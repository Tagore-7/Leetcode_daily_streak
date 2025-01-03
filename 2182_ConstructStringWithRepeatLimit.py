#You are given a string s and an integer repeatLimit. Construct a new string repeatLimitedString using the characters of s such that no letter appears more than repeatLimit times in a row. You do not have to use all characters from s.
#
#Return the lexicographically largest repeatLimitedString possible.
#
#A string a is lexicographically larger than a string b if in the first position where a and b differ, string a has a letter that appears later in the alphabet than the corresponding letter in b. If the first min(a.length, b.length) characters do not differ, then the longer string is the lexicographically larger one.
#
# 
#
#Example 1:
#
#Input: s = "cczazcc", repeatLimit = 3
#Output: "zzcccac"
#Explanation: We use all of the characters from s to construct the repeatLimitedString "zzcccac".
#The letter 'a' appears at most 1 time in a row.
#The letter 'c' appears at most 3 times in a row.
#The letter 'z' appears at most 2 times in a row.
#Hence, no letter appears more than repeatLimit times in a row and the string is a valid repeatLimitedString.
#The string is the lexicographically largest repeatLimitedString possible so we return "zzcccac".
#Note that the string "zzcccca" is lexicographically larger but the letter 'c' appears more than 3 times in a row, so it is not a valid repeatLimitedString.
#Example 2:
#
#Input: s = "aababab", repeatLimit = 2
#Output: "bbabaa"
#Explanation: We use only some of the characters from s to construct the repeatLimitedString "bbabaa". 
#The letter 'a' appears at most 2 times in a row.
#The letter 'b' appears at most 2 times in a row.
#Hence, no letter appears more than repeatLimit times in a row and the string is a valid repeatLimitedString.
#The string is the lexicographically largest repeatLimitedString possible so we return "bbabaa".
#Note that the string "bbabaaa" is lexicographically larger but the letter 'a' appears more than 2 times in a row, so it is not a valid repeatLimitedString.
# 
#
#Constraints:
#
#1 <= repeatLimit <= s.length <= 105
#s consists of lowercase English letters.
#

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        sarray = [0] * 26

        for char in s:
            sarray[ord(char) - 97] += 1

        news = []
        ptr = 0
        for i in range(25, -1, -1):
            count = 0
            while sarray[i]:
                if count < repeatLimit:
                    news.append(chr(i + 97))
                    count += 1
                    sarray[i] -= 1
                else:
                    found = False
                    count = 0
                    for j in range(i - 1, -1, -1):
                        if sarray[j]:
                            if count < repeatLimit:
                                news.append(chr(j + 97))
                                sarray[j] -= 1
                                count = 0
                                found = True
                                break
                    if not found:
                        break
        return "".join(news)