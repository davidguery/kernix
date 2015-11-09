import sys
import json
import os
from apiclient.discovery import build

# Google API key to access API request
api_key = sys.argv[2]#YOUR_API_KEY 

# path where data are stored
data_path='/Users/davidguery2/MesDocuments/entretient_embauche/kernix/data/'

# take in argument youtube channel ID
cha_id = sys.argv[1]

# request details of a youtube channel to extract the channel playlist ID of uploaded videos
youtube = build('youtube', 'v3', developerKey=api_key)

cha_request = youtube.channels().list(part='contentDetails', id=cha_id)
cha_response = cha_request.execute()

items = cha_response['items'][0]
playlistId = items['contentDetails']['relatedPlaylists']['uploads']

# Extract uploaded video list of a channel and get each video inforamtion and comments with get_video_info_api_youtube.py
nResPerPage = 50
play_request = youtube.playlistItems().list(part='contentDetails', playlistId=playlistId, maxResults=nResPerPage)
play_get = play_request.execute()
play_response = [play_get]
totres = play_get['pageInfo']['totalResults']
nres = nResPerPage

#path through all pages of video in playlist
while totres > nres :
    nextPageToken = play_get['nextPageToken']
    play_request = youtube.playlistItems().list(part='contentDetails', playlistId=playlistId, maxResults=nResPerPage, pageToken=nextPageToken)
    play_get = play_request.execute()
    play_response += [play_get]
    nres += nResPerPage

# Write all the video data and comments in a directory specific for the youtube channel
if not os.path.exists(data_path+cha_id) :
    os.mkdir(data_path+cha_id)
with open(data_path+cha_id+'/video_playlist_'+playlistId+'.json', 'w') as savefile :
    json.dump(play_response, savefile)

video_list = []
for playlist in play_response :
    video_list += playlist.get('items', [])

from get_video_info_api_youtube import get_video_info

for video in video_list :
    get_video_info(video['contentDetails']['videoId'], api_key, data_path+cha_id+'/')
