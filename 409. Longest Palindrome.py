class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)
        oddcount = 0
        for fq in freq.values():
            if fq % 2 == 1:
                oddcount += 1
            
        if oddcount > 1:
                return len(s) - oddcount + 1
        return len(s)
