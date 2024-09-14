class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        first, second = 0, int(sqrt(c))
        while first<= second:
            sum =  first * first + second * second
            if sum == c:
                return True
            elif sum > c:
                second -= 1
            else:
                first += 1
        return False
