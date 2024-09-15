class Solution:
    def findLongestSubString(self, s: str) -> int:
        prefixXOR = 0
        characterMap = [0] * 26
        characterMap[ord("a") - ord("a")] = 1
        characterMap[ord("e") - ord("a")] = 2
        characterMap[ord("i") - ord("a")] = 4
        characterMap[ord("o") - ord("a")] = 8
        characterMap[ord("u") - ord("a")] = 16
        mp = [-1] * 32
        longestSubString = 0

        for i in range(len(s)):
            prefixXOR ^= characterMap[ord(s[i)] - ord("a") ]
            if mp[prefixXOR] == -1 and prefixXOR != 0:
                mp[prefixXOR] = i
            longestSubString = max(longestSubString, i - mp[prefixXOR])
        return longestSubString

