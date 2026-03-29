"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        mInterval = 0
        for i in range(len(intervals)):
            if intervals[i].start < mInterval:
                return False
            mInterval = max(mInterval, intervals[i].end)
        return True