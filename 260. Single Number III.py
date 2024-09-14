class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num

        diff_bit = 1
        print(xor & diff_bit)
        while not(xor & diff_bit):
            diff_bit = diff_bit << 1
            print(diff_bit)
        
        a , b = 0, 0

        for num in nums:
            if num & diff_bit:
                a ^= num
            else:
                b ^= num
        return [a, b]
