# kernix
This repository contain 4 python files using youtube data for "toy" programs.
The two first programs are deidicated to dowload Youtube video data of a Youtube channel.
To use this program you need a google API key provided by google developers.
To extract the uploaded video playlist of a youtube channel and data for each video type :
  $ python get_channels_video_playlist_api_youtube channel_ID API_key
  This save in a specific directory all the youtube video datas and top level comments (wihtout replies) for a given channel.
  
Next, to extract some interesting quantity :
  $ python stat_youtube_channel.py channel_ID
  This extract and calculate some quantity for each video like : the video ID, the number of comments (with replies), the number of views, the number of like and dislike votes, the ratio of comments over the number of views, the ratio of votes over the number of views, the list of word for each comment (without replies), the list and number of occurence of words for all comments (without replies), the video keyword found in comments, and the ratio of video keyword found in comments.
  
And to provide some plots and mean over the entire channel :
  $ python result_from_youtube_channel.py channel_ID
  Provide the distribution histograms of comments word for each video showing the number of times a word appears in comments for words with at least 3 letters which appears more than twice. Also the variation of the ratio of comments as a function of the number of view and the ratio of votes vs the number of view. It give too, the mean and dispersion of ratio of comments, ratio of votes and ratio of keywords that appear in comments.
