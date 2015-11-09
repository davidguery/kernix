#define a method to merged two dictionary, summings values associated to
#same keys in the two dictionary
def sumMerge_dict(d1, d2, merged_fn = lambda x,y:x+y) :
    result = dict(d1)
    for k,v in d2.iteritems() :
        if k in result :
            result[k] = merged_fn(result[k],v)
        else :
            result[k] = v
    return result

#define a method to list and count the number o occurence of words in a string
#contained in the comment structure of a youtube video
def comment_word_count(commentDict) :
    from collections import Counter
    comWordCount = [] #word list and count for 1 comment
    for comment in commentDict :
        for com in comment.get('items', []) :
            comstr = com['snippet']['topLevelComment']['snippet']['textDisplay']
            #wordcount = Counter(comstr.split())
            comWordCount += [Counter(comstr.split())]
    globalWordCount = {} #word list and count for all comments of 1 video
    for wordDict in comWordCount :
        globalWordCount = sumMerge_dict(globalWordCount, wordDict, lambda x,y:x+y)
    return comWordCount, globalWordCount


#
import os
import json
import sys

data_path = '/Users/davidguery2/MesDocuments/entretient_embauche/kernix/data/'

# take in argument Youtube channel ID
channel_id = sys.argv[1] 

# get the comments list of a youtube video
filelist = os.listdir(data_path+channel_id+'/')
comlist = [file for file in filelist if 'comments_on_video' in file]

dictlist = [] # set result structure to 0
for comfile in comlist :
    videoId = comfile[18:-5]

    with open(data_path+channel_id+'/video_'+videoId+'.json') as readfile :
        video = json.load(readfile) # Youtbe video data file

    video_items = video.get('items', [])
    stats = video_items[0]['statistics'] #extract youtube video stats
    if 'tags' in video_items[0]['snippet'] : #extract keyword associated with video
        tags = video_items[0]['snippet']['tags']
    else :
        tags = ['']

    #define the saving tructure and keys
    dictResult = {'ID':'', 'commentCount':0., 'viewCounts':0., 'likeCount':0., 'dislikeCount':0., '%_vote':0., '%_comment':0., 'listCommentWord':[], 'commentsWord': {}, 'matchingWordInTags': [], 'ratio_wordInTags': 0.}

    dictResult['commentCount'] = float(stats['commentCount'])
    dictResult['viewCount'] = float(stats['viewCount'])
    dictResult['likeCount'] = float(stats['likeCount'])
    dictResult['dislikeCount'] = float(stats['dislikeCount'])
    dictResult['%_vote'] = (float(stats['likeCount'])+float(stats['dislikeCount']))/float(stats['viewCount'])#*100.
    dictResult['%_comment'] = float(stats['commentCount'])/float(stats['viewCount'])#*100.

    with open(data_path+channel_id+'/'+comfile) as readcom :
        comments = json.load(readcom) #youtube video comment file

    #Extract the list of word from video comments
    dictResult['listCommentWord'], dictResult['commentsWord'] = comment_word_count(comments)
    dictResult['ID'] = videoId

    #test if their is worlds in common between comments and video keyword
    matchingWord = [word for word in dictResult['commentsWord'].keys() if word in tags]
    ratio_wordInTags = [len(matchingWord)/len(tags)]
    dictResult['matchinWordInTags'] = matchingWord
    dictResult['ratio_wordInTags'] = ratio_wordInTags
    
    dictlist += [dictResult]

#Saving results
with open(data_path+channel_id+'/Statistics_and_commentWord.json', 'w') as savefile :
    json.dump(dictlist, savefile) 
