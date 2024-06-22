class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        ans = 0
        org = x
        while x > 0:
            rem = x % 10 
            x = x // 10
            ans += rem
        if org % ans == 0:
            return ans
        return -1
            
