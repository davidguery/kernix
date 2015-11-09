# kernix
This repository contain toy programme on data analysis of Youtube data.
All programs are in python language. to make them work you need an API key from google developers.
It consist in 4 files, 2 to get youtube video data of a chosen youtube channel, and two to use them to do some calculation.
To get data from all videos of a channel just type :
  $ python get_channels_video_playlist_api_youtube.py channel_ID API_key
  
To extract some stats from video data and comments, type :
  $ python stat_youtube_channel.py channel_ID
  This will save a dictionary containing for each video : its ID, the ratio of comments over views, the ratio of votes over views, the number of views, the number of comments, the number of like and dislike vote, the list of word for each top level comments, and the list of word with number of occurence of all the comments of the video.
  
  $ python result_from_youtube_channel.py channel_ID
  This will plot the ditribution histogram of words with at least 3 letters which appears more than twice in all comments for each video. It will also plot the ratio of comments vs the number of view and the ratio of votes vs the number of view on the channel. It calculate the mean ratio of comments and the mean ratio of votes with dispersion.
