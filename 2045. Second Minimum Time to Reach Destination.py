class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        edge_map = defaultdict(list)
        for v1, v2 in edges:
            edge_map[v1].append(v2)
            edge_map[v2].append(v1)
        cur_time = 0
        res = -1 
        visited_times = defaultdict(list)
        q = deque([1])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node == n:
                    if res != -1:
                        return cur_time
                    res = cur_time
                for nei in edge_map[node]:
                    nei_times = visited_times[nei]
                    if len(nei_times) == 0 or (nei_times[0] != cur_time and len(nei_times) == 1):
                        q.append(nei)
                        nei_times.append(cur_time)
            if (cur_time // change) % 2 == 1:
                cur_time += change - (cur_time % change)
            cur_time += time 
