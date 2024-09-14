class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def back_track(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return 
            if total > target or i == len(candidates):
                return 
            cur.append(candidates[i])
            back_track(i+1, cur, total + candidates[i])
            cur.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            back_track(i + 1, cur, total)
        back_track(0, [], 0)
        return res
