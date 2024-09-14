class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n  = len(stones)

        adj_list = [[] for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                if stones[i][0] ==  stones[j][0] or stones[i][1] == stones[j][1]:
                    adj_list[i].append(j)
                    adj_list[j].append(i)

        no_of_conn_comp = 0
        visit = [False] * n

        def dfs(stone):
            visit[stone] = True
            for nei in adj_list[stone]:
                if not visit[nei]:
                    dfs(nei)
        
        for i  in range(n):
            if not visit[i]:
                dfs(i)
                no_of_conn_comp += 1

        return n - no_of_conn_comp
