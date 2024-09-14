class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        count = 0
        c_ind = [i for i in range(len(s)) if s[i] == c]
        for i in range(len(c_ind)):
            count += len(c_ind) - i
        return count
