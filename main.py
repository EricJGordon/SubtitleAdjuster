import re
from time_format import TimeFormat

f = open("subtitles.srt", "r")
lines = f.readlines()
for line in lines:
    x = re.findall(r"\d{2}:\d{2}:\d{2},\d{3}", line)

    if x:
        print("Yes - A match!")
        time1 = TimeFormat(x[0])
        time2 = TimeFormat(x[1])
        print("test", time2.hours, time2.minutes, time2.seconds, time2.milliseconds)
    else:
        print("No match")

    print(line)
