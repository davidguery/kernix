def plot_histo_from_dict(d, width, wordOccure, wordLength, savepath) :
    import pylab as pl
    import numpy as np

    cutd = dict((k, v) for k, v in d.items() if v >= wordOccure and len(k) >= wordLength)
    X = np.arange(len(cutd))*2.
    fig = pl.figure()
    fig.set_size_inches(len(cutd)*0.2,10)
    pl.bar(X, cutd.values(), align='center', width=width)
    pl.xticks(X, cutd.keys(), rotation='vertical', fontsize='small')
    ymax = max(cutd.values()) + 1
    pl.ylim(0, ymax)
    pl.xlim(0-width/2., len(cutd)+width/2.)
    #pl.show()
    pl.savefig(savepath, orientation='landscape', format='PDF', bbox_inches='tight')
    pl.close()
    return

import json
import sys
import pylab as pl
import numpy as np

data_path = '/Users/davidguery2/MesDocuments/entretient_embauche/kernix/data/'

channel_id = sys.argv[1]

with open(data_path+channel_id+'/Statistics_and_commentWord.json') as readcom :
    com_stats = json.load(readcom)

# for video in com_stats :
#     plot_histo_from_dict(video['commentsWord'], 1, 2, 3, data_path+channel_id+'/Occurence_of_words_in_comments_for_video_'+video['ID']+'.pdf')

pl.plot([video['viewCount'] for video in com_stats],[video['%_comment'] for video in com_stats], 'bo')
pl.xlabel('Number of view')
pl.ylabel('Comment ratio')
pl.savefig(data_path+channel_id+'/Views_vs_comments.pdf', format='PDF',bbox_inches='tight')
pl.close()

pl.plot([video['viewCount'] for video in com_stats],[video['%_vote'] for video in com_stats], 'bo')
pl.xlabel('Number of view')
pl.ylabel('Vote ratio')
pl.savefig(data_path+channel_id+'/Views_vs_votes.pdf', format='PDF',bbox_inches='tight')
pl.close()

mean_comment_ratio = np.mean([video['%_comment'] for video in com_stats])
comment_ratio_dev = np.std([video['%_comment'] for video in com_stats])
mean_vote_ratio = np.mean([video['%_vote'] for video in com_stats])
vote_ratio_dev = np.std([video['%_vote'] for video in com_stats])
mean_ratio_wordInTags = np.mean([video['ratio_wordInTags'] for video in com_stats])
wordInTags_dev = np.std([video['ratio_wordInTags'] for video in com_stats])


with open(data_path+channel_id+'/Ratios_for_comment_and_vote.txt', 'w') as ratio_file :
    ratio_file.write("Comment ratio is %8.5f +- %8.5f of video's view. " % (mean_comment_ratio, comment_ratio_dev))
    ratio_file.write("Vote ratio is %8.5f +- %8.5f of video's view. " % (mean_vote_ratio, vote_ratio_dev))
    ratio_file.write("Comments word in video tags is %d. " % len([video['matchingWordInTags'] for video in com_stats])/float(len(com_stats)))

