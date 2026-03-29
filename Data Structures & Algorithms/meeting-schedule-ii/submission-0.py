"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        schedule = []
        for event in intervals:
            schedule.append((event.start,1))
            schedule.append((event.end,0))
        res = tmp = 0
        schedule.sort()
        for event in schedule:
            time, action = event
            if action == 1:
                tmp +=1
            else:
                tmp -=1
            res = max(res,tmp)
        return res

        