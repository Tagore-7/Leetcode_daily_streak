#You are given a string s consisting of lowercase English letters.
#
#Your task is to find the maximum difference diff = freq(a1) - freq(a2) between the frequency of characters a1 and a2 in the string such that:
#
#a1 has an odd frequency in the string.
#a2 has an even frequency in the string.
#Return this maximum difference.
#
# 
#
#Example 1:
#
#Input: s = "aaaaabbc"
#
#Output: 3
#
#Explanation:
#
#The character 'a' has an odd frequency of 5, and 'b' has an even frequency of 2.
#The maximum difference is 5 - 2 = 3.
#Example 2:
#
#Input: s = "abcabcab"
#
#Output: 1
#
#Explanation:
#
#The character 'a' has an odd frequency of 3, and 'c' has an even frequency of 2.
#The maximum difference is 3 - 2 = 1.
# 
#
#Constraints:
#
#3 <= s.length <= 100
#s consists only of lowercase English letters.
#s contains at least one character with an odd frequency and one with an even frequency.
#
class Solution:
    def maxDifference(self, s: str) -> int:
        smap =  defaultdict(int)

        for ch in s:
            smap[ch] += 1

        even_map, odd_map = defaultdict(int), defaultdict(int)

        for key, val in smap.items():
            if val % 2:
                odd_map[key] = val
            else:
                even_map[key] = val

        diff = float("-inf")

        for _, val1 in even_map.items():
            for _, val2 in odd_map.items():
                diff = max(diff, val2 - val1)

        return diff


class Solution:
    def maxDifference(self, s: str) -> int:
        c = Counter(s)
        maxOdd = max(x for x in c.values() if x % 2 == 1)
        maxEven = min(x for x in c.values() if x % 2 == 0)
        return maxOdd - maxEven

