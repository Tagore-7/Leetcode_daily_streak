#Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
#
#A shift on s consists of moving the leftmost character of s to the rightmost position.
#
#For example, if s = "abcde", then it will be "bcdea" after one shift.
# 
#
#Example 1:
#
#Input: s = "abcde", goal = "cdeab"
#Output: true
#Example 2:
#
#Input: s = "abcde", goal = "abced"
#Output: false
# 
#
#Constraints:
#
#1 <= s.length, goal.length <= 100
#s and goal consist of lowercase English letters.
#
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        # length = len(s)
        # for _ in range(length):
        #     s = s[1:] + s[0]
        #     if s == goal:
        #         return True
        # return False
        double_s = s + s

        return double_s.find(goal) != -1


