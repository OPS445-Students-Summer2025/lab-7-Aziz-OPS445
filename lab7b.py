#!/usr/bin/env python3
# lab7b.py
# OPS445 Lab 7 - Investigation 1 - Part 2
# Created by Aziz

class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        if not all(isinstance(x, int) for x in (hours, minutes, seconds)):
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

def add_times(t1, t2):
    """Pure function: returns a new Time object with the sum of t1 and t2"""
    total_seconds = t1.to_seconds() + t2.to_seconds()
    return Time(0, 0, total_seconds)

def change_time(t1, seconds):
    """Modifier function: modifies t1 by adding seconds to it"""
    total_seconds = t1.to_seconds() + seconds
    t1.hours = total_seconds // 3600
    t1.minutes = (total_seconds % 3600) // 60
    t1.seconds = total_seconds % 60

def format_time(t):
    """Returns a string representation of a Time object"""
    return f"{t.hours:02}:{t.minutes:02}:{t.seconds:02}"
