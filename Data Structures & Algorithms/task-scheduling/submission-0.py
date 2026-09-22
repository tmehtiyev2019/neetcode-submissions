class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()
        while maxHeap or q:
            time += 1
            if not maxHeap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time

# Input: tasks = ["A","A","A","B","C"], n = 3

# Output: 9

# char_dict ={
#     "A":3
#     "B":1
#     "C":1
# }

# for key char_dict:
#     if char_dict[key]:

# A:1, A:5, A:9, B: 10, C: 11

# [1, 5, 9, 10, 11]
# [1, 4, 4, 1, 1]



        