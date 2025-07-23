#!/usr/bin/env python3
# Student ID: akelifa-haji-imam

class Time:
    """Simple time class with hour, minute, second"""

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def format_time(self):
        return f"{self.hour:02}:{self.minute:02}:{self.second:02}"

    def time_to_sec(self):
        return self.hour * 3600 + self.minute * 60 + self.second

    def change_time(self, seconds):
        total = self.time_to_sec() + seconds
        new_time = sec_to_time(total)
        self.hour = new_time.hour
        self.minute = new_time.minute
        self.second = new_time.second
        return None

    def sum_times(self, t2):
        total = self.time_to_sec() + t2.time_to_sec()
        return sec_to_time(total)

    def valid_time(self):
        return (0 <= self.hour < 24) and (0 <= self.minute < 60) and (0 <= self.second < 60)

def sec_to_time(seconds):
    """Convert seconds to Time object"""
    minutes, sec = divmod(seconds, 60)
    hour, minute = divmod(minutes, 60)
    return Time(hour, minute, sec)
