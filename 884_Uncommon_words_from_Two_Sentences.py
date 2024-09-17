#A sentence is a string of single-space separated words where each word consists only of lowercase letters.
#
#A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
#
#Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.
#
# 
#
#Example 1:
#
#Input: s1 = "this apple is sweet", s2 = "this apple is sour"
#
#Output: ["sweet","sour"]
#
#Explanation:
#
#The word "sweet" appears only in s1, while the word "sour" appears only in s2.
#
#Example 2:
#
#Input: s1 = "apple apple", s2 = "banana"
#
#Output: ["banana"]
#
# 
#
#Constraints:
#
#1 <= s1.length, s2.length <= 200
#s1 and s2 consist of lowercase English letters and spaces.
#s1 and s2 do not have leading or trailing spaces.
#All the words in s1 and s2 are separated by a single space.

# My first solution:


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1_map = {}
        s1, s2 = s1.split(), s2.split()
        for s in s1:
            if s not in s1_map:
                s1_map[s] = 0
            s1_map[s] += 1
        for s in s2:
            if s not in s1_map:
                s1_map[s] = 0
            s1_map[s] += 1
        ans = []
        for key, value in s1_map.items():
            if value == 1:
                ans.append(key)
        return ans




# leetcode editorial 

class Solution(object):
    def uncommonFromSentences(self, A, B):
        count = Counter(A.split())
        count += Counter(B.split())
        return [word for word in count if count[word] == 1]






























