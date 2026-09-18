class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        k_array = []
        res = []

        for p in points:
            dist = p[0]**2 + p[1]**2
            if len(k_array) < k:
                k_array.append((p, dist))
            elif k_array[-1][1] > dist:
                k_array.pop()
                k_array.append(((p, dist)))
            k_array.sort(key = lambda a:a[1]) #O(logk)
        
        for k in k_array:
            res.append((k[0]))

        return res

            




# points = [[0,2],[2,2]], k = 1

# origin: 0, 0

# ditance: [2, 2.86] 

# dict {[0,2]: 2,[2,2]: 2.8 }

# sort the dict by values
# get the top k keys

# time comp

        