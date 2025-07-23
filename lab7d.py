#!/usr/bin/env python3
# Student ID: akelifa-haji-imam

class Time:
    """Simple time class with hour, minute, second"""

    def __init__(self, hour=0, minute=0, second=0):
=======
# Student ID: [seneca_id] 
class Time:
    """Simple object type for time of the day.
        data attributes: hour, minute, second
        function attributes: __init__, __str__, __repr__
                            time_to_sec, format_time,
                            change_time, sum_time
    """
    def __init__(self,hour=12,minute=0,second=0):
        """constructor for time object""" 

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
=======
        """Return time object (t) as a formatted string"""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def sum_times(self, t2):
        """Add two time objests and return the sum."""
        self_sec = self.time_to_sec()
        t2_sec = t2.time_to_sec()
        sum = sec_to_time(self_sec + t2_sec)
        return sum

    def change_time(self, seconds):
        time_seconds = self.time_to_sec()
        nt = sec_to_time(time_seconds + seconds)
        self.hour, self.minute, self.second = nt.hour, nt.minute, nt.second 
        return None

    def time_to_sec(self):
        '''convert a time object to a single integer representing the 
        number of seconds from mid-night'''
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def valid_time(self):
        """check for the validity of the time object attributes:
        24 > hour > 0, 60 > minute > 0, 60 > second > 0 """
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.minute >= 60 or self.second >= 60 or self.hour >= 24:
            return False
        return True

def sec_to_time(seconds):
    '''convert a given number of seconds to a time object in 
        hour, minute, second format'''
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

