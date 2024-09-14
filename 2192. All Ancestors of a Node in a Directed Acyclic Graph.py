class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        res = [[] for _ in range(n)]
        # print(res)
        graph = [[] for _ in range(n)]
        # print(graph)

        for edge in edges:
            # print(edge)
            graph[edge[0]].append(edge[1])
            # print(graph)

        for i in range(n):
            self.dfs(graph, i, i, res, [False] * n)

        for i in range(n):
            res[i].sort()


        return res


    def dfs(self, graph, parent, curr, res, visit):
        # print(graph)
        # print(parent) # i 
        # print(curr) # i 
        # print(res)
        # print(visit)
        visit[curr] = True
        # print(visit)
        for dest in graph[curr]:
            # print(dest)
            if not visit[dest]:
                res[dest].append(parent)
                self.dfs(graph, parent, dest, res, visit)


        
