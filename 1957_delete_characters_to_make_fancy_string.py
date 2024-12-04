#A fancy string is a string where no three consecutive characters are equal.
#
#Given a string s, delete the minimum possible number of characters from s to make it fancy.
#
#Return the final string after the deletion. It can be shown that the answer will always be unique.
#
# 
#
#Example 1:
#
#Input: s = "leeetcode"
#Output: "leetcode"
#Explanation:
#Remove an 'e' from the first group of 'e's to create "leetcode".
#No three consecutive characters are equal, so return "leetcode".
#Example 2:
#
#Input: s = "aaabaaaa"
#Output: "aabaa"
#Explanation:
#Remove an 'a' from the first group of 'a's to create "aabaaaa".
#Remove two 'a's from the second group of 'a's to create "aabaa".
#No three consecutive characters are equal, so return "aabaa".
#Example 3:
#
#Input: s = "aab"
#Output: "aab"
#Explanation: No three consecutive characters are equal, so return "aab".
# 
#
#Constraints:
#
#1 <= s.length <= 105
#s consists only of lowercase English letters.
#
class Solution:
    def makeFancyString(self, s: str) -> str:
        res = []
        count = 0
        prev = None

        for ch in s:
            if not prev:
                prev = ch
                count = 1
                res.append(ch)
            elif prev:
                if prev == ch:
                    count += 1
                    if count < 3:
                        res.append(ch)
                else:
                    prev = ch
                    count = 1
                    res.append(ch)

        return "".join(res)

class Solution:
    def makeFancyString(self, s: str) -> str:
        res = []
        count = 0
        prev = s[0]

        for ch in s:
            # if not prev:
            #     prev = ch
            #     count = 1
            #     res.append(ch)

            if prev == ch:
                count += 1
                if count < 3:
                    res.append(ch)
            else:
                prev = ch
                count = 1
                res.append(ch)

        return "".join(res)

