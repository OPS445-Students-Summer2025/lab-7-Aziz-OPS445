#!/usr/bin/env python3
# lab7c.py
# OPS445 Lab 7 - Investigation 1 - Part 3
# Created by Aziz

class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        # Validate input types
        if not all(isinstance(i, int) for i in (hours, minutes, seconds)):
            raise TypeError("Hours, minutes, and seconds must be integers")
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def to_seconds(self):
        """Convert time to total number of seconds."""
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def __str__(self):
        """Format time as HH:MM:SS."""
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

def time_to_sec(t):
    """Convert a Time object to total seconds."""
    return t.hours * 3600 + t.minutes * 60 + t.seconds

def sec_to_time(seconds):
    """Convert seconds to a Time object."""
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    return Time(hours, minutes, secs)

def sum_times(t1, t2):
    """Pure function: returns a new Time object with the sum of t1 and t2."""
    total_seconds = time_to_sec(t1) + time_to_sec(t2)
    return sec_to_time(total_seconds)

def change_time(t1, seconds):
    """Modifier function: modifies t1 by adding seconds."""
    total_seconds = time_to_sec(t1) + seconds
    new_time = sec_to_time(total_seconds)
    t1.hours, t1.minutes, t1.seconds = new_time.hours, new_time.minutes, new_time.seconds

def format_time(t):
    """Return a formatted string HH:MM:SS for Time object."""
    return f"{t.hours:02}:{t.minutes:02}:{t.seconds:02}"
