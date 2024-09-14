class Solution:
    def getLucky(self, s: str, k: int) -> int:
        alphabets_map = {chr(i): i - 96 for i in range(97, 123)}
        digits = ""
        for c in s:
            digits += str(alphabets_map[c])
        for _ in range(k):
            res_sum = 0
            for digit in digits:
                res_sum += int(digit)
            digits = str(res_sum)
            
        return int(digits) 

