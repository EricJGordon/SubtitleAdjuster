import re
import sys
import fileinput
from time_format import TimeFormat


def time_repl(match):
    return TimeFormat(match.group(0)).offset_by(sys.argv[2])


for line in fileinput.input(sys.argv[1], inplace=True):
    line = re.sub(r"\d{2}:\d{2}:\d{2},\d{3}", time_repl, line)
    print(line, end='')
