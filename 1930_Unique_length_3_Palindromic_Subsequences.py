#Given a string s, return the number of unique palindromes of length three that are a subsequence of s.
#
#Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.
#
#A palindrome is a string that reads the same forwards and backwards.
#
#A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
#
#For example, "ace" is a subsequence of "abcde".
# 
#
#Example 1:
#
#Input: s = "aabca"
#Output: 3
#Explanation: The 3 palindromic subsequences of length 3 are:
#- "aba" (subsequence of "aabca")
#- "aaa" (subsequence of "aabca")
#- "aca" (subsequence of "aabca")
#Example 2:
#
#Input: s = "adc"
#Output: 0
#Explanation: There are no palindromic subsequences of length 3 in "adc".
#Example 3:
#
#Input: s = "bbcbaba"
#Output: 4
#Explanation: The 4 palindromic subsequences of length 3 are:
#- "bbb" (subsequence of "bbcbaba")
#- "bcb" (subsequence of "bbcbaba")
#- "bab" (subsequence of "bbcbaba")
#- "aba" (subsequence of "bbcbaba")
# 
#
#Constraints:
#
#3 <= s.length <= 105
#s consists of only lowercase English letters.
#
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        letters = set(s)
        ans = 0

        for letter in letters:
            i, j = s.index(letter), s.rindex(letter)
            between = set()

            for k in range(i + 1, j):
                between.add(s[k])
            ans += len(between)

        return ans



        if len(s) < 3:
            return 0

        count = 0
        wset = set()
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                for k in range(j + 1, len(s)):
                    word = s[i] + s[j] + s[k]
                    # print(word, word[::-1])
                    if word == word[::-1]:
                        if word not in wset:
                            wset.add(word)
                            count += 1

        return count

