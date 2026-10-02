class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda x: x[0])
        res = []
        if len(intervals) == 0:
            return res

        merge_start = intervals[0][0]
        merge_end = intervals[0][1]

        for start, end in intervals:
            if start > merge_end:
                res.append([merge_start,merge_end])
                merge_start = start
                merge_end = end

                
            elif merge_start > end:
                res.append([start, end])

            else:
                merge_start = min(start, merge_start)
                merge_end = max(end, merge_end)
        res.append([merge_start,merge_end])
        return res


# # notes
# 1. the last one was not added

        