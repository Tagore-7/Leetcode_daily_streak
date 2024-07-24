class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        pairs = []

        for i in range(len(nums)):
            number = str(nums[i])
            formed = ''
            for j in range(len(number)):
                formed = formed + str(mapping[int(number[j])])
            mapped_value = int(formed)
            pairs.append((mapped_value, i))

        pairs.sort()
        ans = []
        for pair in pairs:
            ans.append(nums[pair[1]])
        return ans
