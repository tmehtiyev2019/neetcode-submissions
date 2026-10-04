class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        q = deque()
        visited =[0] * n
        conn_comp = 0
        adj_list = defaultdict(list)

        for n1, n2 in edges:
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)

        while sum(visited) != n:
            #logic to subtrack visited form missing
            #brute force approach
            for i in range(len(visited)):
                if visited[i]==0:
                    q.append(i) 
                    break     
            conn_comp += 1
            while q:
                node = q.popleft()
                visited[node] = 1
                for j in adj_list[node]:
                    if visited[j]!= 1:
                        q.append(j)
        return conn_comp






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









        