#!/usr/bin/env python3

class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def time_to_sec(self):
        """Convert time to total seconds."""
        return self.hour * 3600 + self.minute * 60 + self.second

    def format_time(self):
        """Return time formatted as HH:MM:SS."""
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"

    def sum_times(self, t2):
        """Add another Time object t2 to self and return new Time object."""
        total_seconds = self.time_to_sec() + t2.time_to_sec()
        return sec_to_time(total_seconds)

    def change_time(self, seconds):
        """Add seconds to the current time and update the time object."""
        total_seconds = self.time_to_sec() + seconds
        new_time = sec_to_time(total_seconds)
        self.hour = new_time.hour
        self.minute = new_time.minute
        self.second = new_time.second

    def valid_time(self):
        """Check if the current time object is valid."""
        if (0 <= self.hour <= 23) and (0 <= self.minute <= 59) and (0 <= self.second <= 59):
            return True
        return False

def sec_to_time(seconds):
    """Convert total seconds to a Time object."""
    seconds %= 86400  # wrap around 24 hours
    hour = seconds // 3600
    seconds %= 3600
    minute = seconds // 60
    second = seconds % 60
    return Time(hour, minute, second)
