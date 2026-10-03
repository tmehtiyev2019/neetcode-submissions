"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        merge = True
        if len(intervals) == 0:
            return merge
        intervals.sort(key = lambda x: x.start)
        merge_start = float("-inf")
        merge_end = float("-inf") + 1

        for interval in intervals:
            if merge_start >= interval.end or merge_end <= interval.start:
                merge_start = interval.start
                merge_end = interval.end

            else:
                merge = False
                return merge
        return merge


