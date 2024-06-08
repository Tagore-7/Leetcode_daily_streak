class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        rmap = {0:-1}
        csum = 0

        for i , num in enumerate(nums):
            csum += num
            rem = csum % k
            if rem in rmap:
                if i - rmap[rem] >= 2:
                    return True
            else:
                rmap[rem] = i
        return False
 
