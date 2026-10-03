class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        visited = set()
        for n1, n2 in edges:
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)


        def dfs(n, prev):
            
            if n in visited:
                return False

            visited.add(n)
            for node in adj_list[n]:
                if node != prev:
                    if not dfs(node, n):
                        return False
            return True

        return dfs(0,0) and len(visited) ==n





    
#  where tp start?       

# 2 rules:

# 1. no cycle: the only tricky part id unidirected
# 2. 1 component: if anythign left from visited it measn it is not accessable.



# adj_mat = {
#     0:[1,2,3],
#     1:[0,4],
#     2:[0],
#     3:[0],
#     4:[0]
# }





# Goal: a func to check if teh given edges make up a valid tree



# Constr. clarifications.
# 1. if empty list then Valid?
# 2. since undirected [0,1] also means [1,0]
# 3. Can we have self connection such as [1,1]
# 4. What if we have a serate node not connecte to the rest of the tree? or seperate pair



# generalization of the def.:

# if we cna detect a loop, it means it is not a valid tree: 
#     assumption: this is necessary cond. if not we need to compe up woth other conds as well.



# Desc.

# Note:
# Def. of valid tree: thrers is a root node and nodes are connected to only parent and child nodes

# Edges: undirected
# examp 1
# n=3
# [[0,1],[0,2],[1,3]] -> Valid

# examp 1
# n=4
# [[0,1],[1,2],[1,3],[0,3]] -> invalid

        