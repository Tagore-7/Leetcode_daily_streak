class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        dup = s + s
        dup = dup[1:-1]
        print(dup)
        if s in dup:
            return True
        return False
