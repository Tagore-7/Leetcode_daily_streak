class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        def helper(m):
            res = 0
            l = 0
            for r in range(len(nums)):
                while nums[r] - nums[l] > m:
                    l += 1
                res += r - l
            return res
        l , r = 0,max(nums)
        while l < r:
            m = l +((r - l) // 2)
            pairs = helper(m)
            if pairs >= k:
                r = m 
            else:
                l = m +1
        return r

            

