class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cyc_len =  2 * (n - 1)
        time = time % cyc_len

        if time < n:
            return time + 1
        else:
            return 2 * n - time - 1
        
