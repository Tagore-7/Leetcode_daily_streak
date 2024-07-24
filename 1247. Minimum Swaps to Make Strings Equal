class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        if s1 == s2:
            return 0
        x, y = 0, 0
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                continue
            if s1[i] == 'x':
                x += 1
            else:
                y  += 1
        if (x+y) % 2 ==1:
            return -1
        return int((x+1) // 2 + (y + 1) // 2)
