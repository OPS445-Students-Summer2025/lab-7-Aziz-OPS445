#!/usr/bin/env python3
# lab7f.py
# OPS445 Lab 7 - Investigation 3 - Part 1
# Created by Aziz

class Time:
    """Simple time class with hour, minute, second"""

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        """Return formatted string HH:MM:SS"""
        return f"{self.hour:02}:{self.minute:02}:{self.second:02}"

    def __repr__(self):
        """Return formatted string HH.MM.SS for debugging/testing"""
        return f"{self.hour:02}.{self.minute:02}.{self.second:02}"

    def time_to_sec(self):
        """Return total seconds for this time object"""
        return self.hour * 3600 + self.minute * 60 + self.second

    def sum_times(self, t2):
        """Return a new Time object which is sum of self and t2"""
        total_seconds = self.time_to_sec() + t2.time_to_sec()
        return sec_to_time(total_seconds)

    def __add__(self, t2):
        """Overload the '+' operator to add two Time objects"""
        return self.sum_times(t2)

def sec_to_time(seconds):
    """Convert seconds to Time object"""
    minutes, sec = divmod(seconds, 60)
    hour, minute = divmod(minutes, 60)
    return Time(hour, minute, sec)
