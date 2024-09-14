class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)

        for i in range(len(edges)):
            src, dest =  edges[i]
            graph[src].append((dest, succProb[i]))
            graph[dest].append((src, succProb[i]))

        visit = set()
        max_heap = [(-1, start_node)]

        while max_heap:
            prob, curr = heapq.heappop(max_heap)
            visit.add(curr)
            if curr == end_node:
                return prob * -1 

            for nei, nprob in graph[curr]:
                if nei not in visit:
                    heapq.heappush(max_heap, (prob * nprob, nei))
                

        return 0
