import re
import fileinput
from time_format import TimeFormat

# print(TimeFormat("00:05:47,198").offset_by("00:05:47,198"))
for line in fileinput.input("subtitles.srt", inplace=True):
    numToReplace = re.findall(r"(\d{2}:\d{2}:\d{2},\d{3})", line)
    for num in numToReplace:
        line = re.sub(r"(\d{2}:\d{2}:\d{2},\d{3})", TimeFormat(num).offset_by("00:00:08,123"), line, 1)

    print(line, end='')

