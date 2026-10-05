class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, node):
        cur = node
        while cur != self.parent[cur]:
            cur = self.parent[cur]
        return cur
    
    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        if self.rank[pv] > self.rank[pu]:
            self.parent[pu] = pv
        elif self.rank[pv] < self.rank[pu]:
            self.parent[pv] = pu
        else:
            self.parent[pv] = pu
            self.rank[pu] += 1
        return True 

            



class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        res = n
        for u, v in edges:
            if dsu.union(u,v):
                res -= 1
        return res













# class Solution:
#     def countComponents(self, n: int, edges: List[List[int]]) -> int:

#         q = deque()
#         visited =set()
#         conn_comp = 0
#         adj_list = defaultdict(list)

#         for n1, n2 in edges:
#             adj_list[n1].append(n2)
#             adj_list[n2].append(n1)

#         for i in range(n):
#             if i in visited:
#                 continue
#             q.append(i)
#             conn_comp += 1
#             visited.add(i)
#             while q:
#                 node = q.popleft()
#                 visited.add(node)
#                 for j in adj_list[node]:
#                     if j not in visited:
#                         q.append(j)
#                         visited.add(node)
#         return conn_comp


# Time complexity: E + V
# Space complexity: E + v





# 1: connected comp: if we can acces any node forma. given node


# the issue is differentiate 2 from 3, 4
# q: how to count it. the definition of the counter update
# q: how to initialize hwa tis missing in visite


# adj_list={
#     0:[1],
#     1:[0,2]
#     2:[1]
#     3:[4]
#     4:[3]

# }









        