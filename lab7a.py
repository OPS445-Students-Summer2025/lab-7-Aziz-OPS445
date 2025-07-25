#!/usr/bin/env python3
# lab7a.py
# OPS445 Lab 7 - Investigation 1 - Part 1
# Created by Aziz

def main():
    print("Lab 7 Investigation 1 Part 1")

if __name__ == '__main__':
    main()


class Time:
    """Simple object type for time of the day.
       data attributes: hour, minute, second
    """
    def __init__(self, hour=12, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    """Return time object (t) as a formatted string"""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def sum_times(t1, t2):
    """Add two time objects and return the sum."""
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second

    # Carry-over fix
    if sum.second >= 60:
        sum.minute += sum.second // 60
        sum.second %= 60
    if sum.minute >= 60:
        sum.hour += sum.minute // 60
        sum.minute %= 60

    return sum

def valid_time(t):
    """Check for the validity of the time object attributes"""
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.hour >= 24 or t.minute >= 60 or t.second >= 60:
        return False
    return True

