class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        while k:
            heapq.heappush(nums, heappop(nums) + 1)
            k -= 1
        ans = 1

        for num in nums:
            ans = (ans * num) % (10**9 + 7)

        return ans
