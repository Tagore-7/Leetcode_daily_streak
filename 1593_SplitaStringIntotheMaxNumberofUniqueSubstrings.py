#Given a string s, return the maximum number of unique substrings that the given string can be split into.
#
#You can split string s into any list of non-empty substrings, where the concatenation of the substrings forms the original string. However, you must split the substrings such that all of them are unique.
#
#A substring is a contiguous sequence of characters within a string.
#
# 
#
#Example 1:
#
#Input: s = "ababccc"
#Output: 5
#Explanation: One way to split maximally is ['a', 'b', 'ab', 'c', 'cc']. Splitting like ['a', 'b', 'a', 'b', 'c', 'cc'] is not valid as you have 'a' and 'b' multiple times.
#Example 2:
#
#Input: s = "aba"
#Output: 2
#Explanation: One way to split maximally is ['a', 'ba'].
#Example 3:
#
#Input: s = "aa"
#Output: 1
#Explanation: It is impossible to split the string any further.
# 
#
#Constraints:
#
#1 <= s.length <= 16
#
#s contains only lower case English letters.
#
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        
        def dfs(i, cur_set):
            if i == len(s):
                return 0

            res = 0

            for j in range(i, len(s)):
                sub_str = s[i: j + 1]
                if sub_str in cur_set:
                    continue
                cur_set.add(sub_str)
                res = max(res, 1 + dfs(j + 1, cur_set))
                cur_set.remove(sub_str)
            return res 
        return dfs(0, set())
