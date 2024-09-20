#You are given a string s. You can convert s to a 
#palindrome
# by adding characters in front of it.
#
#Return the shortest palindrome you can find by performing this transformation.
#
# 
#
#Example 1:
#
#Input: s = "aacecaaa"
#Output: "aaacecaaa"
#Example 2:
#
#Input: s = "abcd"
#Output: "dcbabcd"
# 
#
#Constraints:
#
#0 <= s.length <= 5 * 104
#s consists of lowercase English letters only.

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        base = 29
        mod = int(1e9 + 7)
        fhash = 0
        rhash = 0
        power = 1
        lindex = -1
        for i, c in enumerate(s):
            fhash = (fhash * base + (ord(c) - ord("a") + 1)) % mod
            rhash = (rhash + (ord(c)- ord("a") + 1) * power ) % mod
            power = (power * base) % mod
            if fhash == rhash:
                lindex = i
        suffix = s[lindex + 1:]
        rsuffix = suffix[::-1]
        return rsuffix + s
