import re
import fileinput
from time_format import TimeFormat

for line in fileinput.input("subtitles.srt", inplace=True):
    x = re.sub(r"\d{2}:\d{2}:\d{2},\d{3}", "00:00:00,000", line)
    print('{}'.format(x), end='')

    # print(line)
