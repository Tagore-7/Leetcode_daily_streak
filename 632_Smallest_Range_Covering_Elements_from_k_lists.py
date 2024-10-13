#You have k lists of sorted integers in non-decreasing order. Find the smallest range that includes at least one number from each of the k lists.
#
#We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a < c if b - a == d - c.
#
# 
#
#Example 1:
#
#Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
#Output: [20,24]
#Explanation: 
#List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
#List 2: [0, 9, 12, 20], 20 is in range [20,24].
#List 3: [5, 18, 22, 30], 22 is in range [20,24].
#Example 2:
#
#Input: nums = [[1,2,3],[1,2,3],[1,2,3]]
#Output: [1,1]
# 
#
#Constraints:
#
#nums.length == k
#1 <= k <= 3500
#1 <= nums[i].length <= 50
#-105 <= nums[i][j] <= 105
#nums[i] is sorted in non-decreasing order.
#
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k = len(nums)
        left, right = nums[0][0]
        min_heap = []
        for i in range(k):
            l = nums[i]
            left = min(left, l[0])
            right = max(right, l[0])
            heapq.heappush(min_heap, (l[0], i, 0))

        res = [left, right]

        while True:
            n, i, idx = heapq.heappop(min_heap)
            if idx == len(nums[i]):
                return res
            idx += 1
            next_val = nums[i][idx]
            heapq.heappush(min_heap, (next_val, i, idx))
            right = max(right, next_val)
            left = min_heap[0][0]
            if right - left < res[1] - res[0]:
                res = [left, right]

