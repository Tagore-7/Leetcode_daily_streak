class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for src, dest in edges:
            adj_list[src].append(dest)

        def dfs(node):
            if node in path:
                return float("inf")
            if node in visit:
                return 0
            
            visit.add(node)
            path.add(node)

            colorIndex = ord(colors[node]) - ord("a")
            colorCount[node][colorIndex] = 1
            
            for nei in adj_list[node]:
                if dfs(nei) == float("inf"):
                    return float("inf")
                for c in range(26):
                    colorCount[node][c] = max(colorCount[node][c], 
                    (1 if c == colorIndex else 0) + colorCount[nei][c])
            path.remove(node)
            return max(colorCount[node])

        n, res = len(colors), 0
        visit, path = set(), set()
        colorCount = [[0]*26 for _ in range(n)]
        for i in range(n):
            res = max(res, dfs(i))

        return -1 if res  == float("inf") else res
