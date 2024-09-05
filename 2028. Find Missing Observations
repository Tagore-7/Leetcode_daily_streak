class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        res = (len(rolls) + n ) * mean  - sum(rolls)
        if res < n or res > 6* n:
            return []
        dismean = res // n
        mod = res % n 
        ans = [dismean]  * n
        for i in range(mod):
            ans[i] += 1
        return ans
