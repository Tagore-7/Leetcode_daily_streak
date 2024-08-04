class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sub_arr = []
        MOD = 10 ** 9 + 7
        for i in range(n):
            sub_sum = 0
            for j in range(i, n):
                sub_sum = (sub_sum + nums[j] ) % MOD 
                sub_arr.append(sub_sum)
        sub_arr.sort()
        print(sub_arr)
        res = 0
        for i in range(left -1 , right):
            res = (res + sub_arr[i] ) % MOD
        return res
