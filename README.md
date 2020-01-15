# SubtitleAdjuster

This program can be used to make small (or big) adjustments to all the time instances contained in a .srt subtitle file for if the audio is slightly out of sync with the video.

As an example, the following command would take the file subtitles.srt and offset each number by an additional one and a half seconds, i.e. the corresponding captions would appear 1.5 seconds later than originally: 

  \> python main.py subtitles.srt 00:00:01,500

The offset amount always has to follow that format of hh:mm:ss,mmm  
(hours then minutes then seconds then milliseconds)
