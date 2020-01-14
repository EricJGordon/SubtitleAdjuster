import re
import sys
import fileinput
from time_format import TimeFormat


def time_repl(match):
    return TimeFormat(match.group(0)).offset_by("00:00:08,123")


for line in fileinput.input(sys.argv[1], inplace=True):
    line = re.sub(r"\d{2}:\d{2}:\d{2},\d{3}", time_repl, line)
    print(line, end='')

# TODO: take file name and offset time as args
