class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        bignumber = int(2e9)
        graph = [[] for _ in range(n)]

        for u , v , w in edges:
            if w != -1:
                graph[u].append((v, w))
                graph[v].append((u, w))

        def dijkstra( graph, src, dest):
            min_dist = [math.inf] * len(graph)
            min_dist[src] = 0
            min_heap = [(0, src)]

            while min_heap:
                d, u = heapq.heappop(min_heap)
                if d < min_dist[u]:
                    continue 
                for v, w in graph[u]:
                    if d + w < min_dist[v]:
                        min_dist[v] = d + w
                        heapq.heappush(min_heap, (min_dist[v], v))
            return min_dist[dest]


        curr_short_dist = dijkstra(graph, source, destination)

        if curr_short_dist < target:
            return []

        if curr_short_dist == target:
            for edge in edges:
                if edge[2] == -1 :
                    edge[2] = bignumber
            return edges
        
        for i, (u, v, w) in enumerate(edges):
            if w != -1:
                continue
            
            edges[i][2] = 1
            graph[u].append((v, 1))
            graph[v].append((u, 1))

            new_distance = dijkstra(graph, source, destination)

            if new_distance <= target:
                edges[i][2] += target - new_distance 
                for j in range(i + 1, len(edges)):
                    if edges[j][2] == -1:
                        edges[j][2] = bignumber
                return edges
        return []

        
