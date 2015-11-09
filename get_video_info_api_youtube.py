
def get_video_info(video_id, api_key, data_path) :
    import sys
    import json
    from apiclient.discovery import build

    #data_path=sys.argv[3] #'/Users/davidguery2/MesDocuments/entretient_embauche/kernix/data/'

    #take in argument a youtube video ID
    #video_id=sys.argv[1]

    #personnal key for API request
    #api_key = sys.argv[2]

    #take youtube pulic information on a given video in a JSON structure in unicode format:
    #definition : 'hd'
    #dimension : '2d', '3d'
    #duration
    #licensedContent : True or False
    #etag
    #ID
    #kind : youtube#video
    #snippet :
        #categoryID
        #channelId
        #channelTitle
        #description
        #title
    #publishedAt
    #thumbnails
    #statistics :
        #commentCount
        #dislikeCount
        #favoriteCount
        #likeCount
        #viewCount
    youtube = build('youtube', 'v3', developerKey=api_key)
    vid_request = youtube.videos().list(id=video_id,part='snippet,statistics')
    vid_response = vid_request.execute()

    #save the video data as a JSON object in a text file
    with open(data_path+'video_'+video_id+'.json', 'w') as savefile :
        json.dump(vid_response, savefile)

        #video = vid_response.get('item', []) # video is a list of dict
        #statistics = video[0]['statistics']

    #take all comments on the video without replies up to a maximum of 100 comments per page
    nResPerPage = 100
    com_request = youtube.commentThreads().list(videoId=video_id, part='snippet', maxResults=nResPerPage, order='relevance', textFormat='plainText')
    com_get = com_request.execute()
    com_response = [com_get]
    totres = com_get['pageInfo']['totalResults']
    nres = nResPerPage
    while totres > nres :
        nextPageToken = com_get['nextPageToken']
        com_request = youtube.commentThreads().list(videoId=video_id, part='snippet', maxResults=nResPerPage, order='relevance', textFormat='plainText', pageToken=nextPageToken)
        com_get = com_request.execute()
        com_response += [com_get]
        nres += nResPerPage

    #save video's comments in a JSON object in a text file
    with open(data_path+'comments_on_video_'+video_id+'.json', 'w') as savecom :
        json.dump(com_response, savecom)
        #comments = com_response.get('item', []) # comments is a list of dict containing each comments details
    return

#Remark : this function crash if video comments are disabled
