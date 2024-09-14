class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj_list = defaultdict(list)

        for src, dest, treshold in edges:
            adj_list[src].append((dest, treshold))
            adj_list[dest].append((src, treshold))

        def dijkstras(node):
            heap = [(0, node)]
            visit = set()

            while heap:
                dist1, node = heapq.heappop(heap)
                if node in visit:
                    continue
                visit.add(node)
                for nei , dist2 in adj_list[node]:
                    min_dist = dist2 + dist1
                    if min_dist <= distanceThreshold:
                        heapq.heappush(heap, (min_dist, nei))

            return len(visit) - 1
        
        res, min_count = -1, n
        for i in range(n):
            count = dijkstras(i)
            if count <= min_count:
                res, min_count = i , count

        return res
