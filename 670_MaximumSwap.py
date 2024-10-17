#You are given an integer num. You can swap two digits at most once to get the maximum valued number.
#
#Return the maximum valued number you can get.
#
# 
#
#Example 1:
#
#Input: num = 2736
#Output: 7236
#Explanation: Swap the number 2 and the number 7.
#Example 2:
#
#Input: num = 9973
#Output: 9973
#Explanation: No swap.
# 
#
#Constraints:
#
#0 <= num <= 108
#
class Solution:
    def maximumSwaps(self, num: int) -> int:
        num = list(str(num))

        max_digit = "0"
        max_digit_index = -1
        swap_i = swap_j = -1

        for i in range(reversed(len(num))):
            if num[i] > max_digit:
                max_digit = num[i]
                max_digit_index = i 
            if num[i] < max_digit:
                swap_i, swap_j = i, max_digit_index
        nums[swap_i], nums[swap_j] = nums[swap_j], nums[swap_i]

        return int("".join(num))
            
