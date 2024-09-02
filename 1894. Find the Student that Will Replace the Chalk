class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k %= sum(chalk)
        n = len(chalk)
        index = 0
        while k > 0:
            if k < chalk[index]:
                return index
            k -= chalk[index]
            index += 1

        return index
        
        
            

