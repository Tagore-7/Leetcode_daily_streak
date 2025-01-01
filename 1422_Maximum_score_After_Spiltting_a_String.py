#Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).
#
#The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.
#
# 
#
#Example 1:
#
#Input: s = "011101"
#Output: 5 
#Explanation: 
#All possible ways of splitting s into two non-empty substrings are:
#left = "0" and right = "11101", score = 1 + 4 = 5 
#left = "01" and right = "1101", score = 1 + 3 = 4 
#left = "011" and right = "101", score = 1 + 2 = 3 
#left = "0111" and right = "01", score = 1 + 1 = 2 
#left = "01110" and right = "1", score = 2 + 1 = 3
#Example 2:
#
#Input: s = "00111"
#Output: 5
#Explanation: When left = "00" and right = "111", we get the maximum score = 2 + 3 = 5
#Example 3:
#
#Input: s = "1111"
#Output: 3
# 
#
#Constraints:
#
#2 <= s.length <= 500
#The string s consists of characters '0' and '1' only.
#

#My own Solution 
class Solution:
    def maxScore(self, s: str) -> int:
        if len(s) == 2:
            if s[0] == "0" and s[1] == "0":
                return 1
            elif s[0] == "1" and s[1] == "1":
                return 1
            elif s[0] == "1" and s[1] == "0":
                return 0
            else:
                return 2

        score = [0] * len(s)
        def cal(left, right):
            res = 0
            for char in left:
                if char == "0":
                    res += 1

            for char in right:
                if char == "1":
                    res += 1
            return res
        for i in range(1, len(s)):
            left, right = s[:i], s[i:]
            score[i] = cal(left, right)

        return max(score)

# Leetcode optimized 

class Solution:
    def maxScore(self, s: str) -> int:
        ones = s.count("1")
        zeros = 0
        ans = 0

        for i in range(len(s) - 1):
            if s[i] == "1":
                ones -= 1
            else:
                zeros += 1

            ans = max(ans, ones + zeros)

        return ans 
