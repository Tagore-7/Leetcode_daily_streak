class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        rsum = 0
        rcount = {0:1}
        for i in range(len(nums)):
            rsum += nums[i]
            rem = rsum % k
            if rem < 0:
                rem += k
            count += rcount.get(rem, 0)
            rcount[rem] = rcount.get(rem,0) + 1
        return count 
