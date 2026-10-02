class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        new_start = newInterval[0]
        new_end = newInterval[1]
        flag = False
        for start, end in intervals:
            if new_end < start: # no overlap
                if flag == False:
                    res.append([new_start, new_end])
                    flag = True
                res.append([start, end])

            elif new_start > end: # no overlap
                res.append([start, end])
            
            else:
                new_start = min(start, new_start)
                new_end = max(end, new_end)
        
        if flag == False:
            res.append([new_start, new_end])
        return res


# new_start = 1
# new_end = 5


        