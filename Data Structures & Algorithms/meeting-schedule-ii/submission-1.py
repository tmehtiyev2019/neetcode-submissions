"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0
        room_count = 1 #Adressed intially heap shoudl have the first slot
        intervals.sort(key = lambda x: x.start) #Adressed: assumption they are not sorted
        heap = [(intervals[0].end, intervals[0].start)]
        # heap = []
        
        for interval in intervals[1:]:
            if interval.start >= heap[0][0]: #Adressed: pay attention to the structure of the heap. do we add it as an object? if yes, this should not subscripable
                heapq.heappop(heap)
                heapq.heappush(heap,(interval.end, interval.start))
            else:
                room_count += 1
                heapq.heappush(heap,(interval.end, interval.start))
        return room_count







#note:

# pay attention to sorting in the heap : Adressed

# Dry Run

# Input: intervals = [(0,40),(5,10),(15,20)] -- sorted []

# Output: 2

# question: do I truly need sorting?
# answer: Yes


        