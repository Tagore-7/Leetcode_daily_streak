class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degree = [0] * n
        # print(degree)

        for road in roads:
            # print(road)
            degree[road[0]] += 1
            degree[road[1]] += 1
        # print(degree)
        cities = list(range(n))
        # print(cities)
        cities.sort(key = lambda x: -degree[x])
        # print(cities)

        imp = 0
        for i in range(n):
            imp += (n-i) * degree[cities[i]]

        return imp
