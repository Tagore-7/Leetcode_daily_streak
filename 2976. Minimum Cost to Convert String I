class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        Map = defaultdict(list)
        for src, tar , cst in zip(original, changed, cost):
            Map[src].append((tar, cst))

        def dijkstras(src):
            heap  = [(0, src)]
            min_cost_map = {}
            while heap:
                cst, nde = heapq.heappop(heap)
                if nde in min_cost_map:
                    continue
                min_cost_map[nde] = cst
                for nei, nei_cost in Map[nde]:
                    heapq.heappush(heap, (cst+ nei_cost, nei))
            return min_cost_map

        Min_cost_map = {c:dijkstras(c) for c in set(source)}
        res = 0
        for src, tar in zip(source, target):
            if tar not in Min_cost_map[src]:
                return -1
            res += Min_cost_map[src][tar]
        return res
