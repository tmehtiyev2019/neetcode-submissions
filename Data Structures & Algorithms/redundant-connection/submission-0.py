
# cycle detection




class DSU:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.rank = [1] * (n+1)

    
    def find(self, n):
        cur = self.parent[n]
        while cur != self.parent[cur]:
            cur = self.parent[cur]
        return cur


    def union(self, n1, n2):
        pn1 = self.find(n1)
        pn2 = self.find(n2)

        if pn1 == pn2:
            return False
        
        if self.rank[pn1] > self.rank[pn2]:
            self.parent[pn2] = pn1

        elif self.rank[pn1] < self.rank[pn2]:
            self.parent[pn1] = pn2

        else:
            self.parent[pn1] = pn2
            self.rank[pn2] += 1

        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges))

        for i, j in edges:
            if not dsu.union(i, j):
                return [i,j]
            




# Dry Run:

# Input: edges = [[1,2],[1,3],[3,4],[2,4]]

# Output: [2,4]



# node_freq = {
#     (1,2) : [0, 0],
#     (1,3) : [0, 1],
#     (3,4) : [0, 2],
#     (2,4) : [0, 3]

# }

# adj_list = {
#     1: [2, 3],
#     2: [1, 4],
#     3: [1, 4],
#     4: [2, 3]
# }


# q = [(1,-1)] --> [(2,1)] 
# node, prev = 1, -1




# Time complexity: V + E
# Space Complexity: V + E



        #stop logic in the while q becasue of the loop







# Notes:
# we cna detect a cycle with an edge

# challenge; how to decide the last edge in the input if we ahve many options?
        