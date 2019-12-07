class TimeFormat:
    def __init__(self, time_str):
        self.hours = time_str[:2]
        self.minutes = time_str[3:5]
        self.seconds = time_str[6:8]
        self.milliseconds = time_str[9:]

