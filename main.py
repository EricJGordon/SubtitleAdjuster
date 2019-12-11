import re
import fileinput
from time_format import TimeFormat

for line in fileinput.input("subtitles.srt", inplace=True):
    times = re.findall(r"(\d{2}:\d{2}:\d{2},\d{3})", line)
    for time in times:
        line = re.sub(r"(\d{2}:\d{2}:\d{2},\d{3})", TimeFormat(time).test(), line, 1)

    print(line, end='')
