# SubtitleAdjuster

This program can be used to make small (or big) adjustments to all the time instances contained in a .srt subtitle file for when the audio is slightly out of sync with the video.

As an example, the following command would take the file subtitles.srt and offset each number by an additional one and a half seconds, so that each caption would appear (and disappear) 1.5 seconds later than originally: 

  \> python main.py subtitles.srt +00:00:01,500
  
While this one would shift things a quarter second earlier:

  \> python main.py subtitles.srt -00:00:00,250

The offset amount always has to follow that format of ±hh:mm:ss,mmm  
(operator then hours then minutes then seconds then milliseconds)
