class TimeFormat:
    def __init__(self, time_str):
        self.hours = int(time_str[:2])
        self.mins = int(time_str[3:5])
        self.secs = int(time_str[6:8])
        self.millis = int(time_str[9:])

        # TODO: add_offset function

    def test(self):
        # print("test", self.hours, self.minutes, self.seconds, self.milliseconds)
        return '(just seconds: ' + self.seconds + ' )'

    def offset_by(self, offset):
        other = TimeFormat(offset)
        temp = self.millis + other.millis
        self.secs += temp // 1000
        self.millis = temp % 1000

        temp = self.secs + other.secs
        self.mins += temp // 60
        self.secs = temp % 60

        temp = self.mins + other.mins
        self.hours += temp // 60
        self.mins = temp % 60

        self.hours = (self.hours + other.hours) % 100
        # hours not guaranteed to be correct in cases of overflow, but realistically not a problem

        # combine and handle leading 0's
