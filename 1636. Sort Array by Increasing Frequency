class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        Map = Counter(nums)
        return sorted(nums, key = lambda x: (Map[x], - x))
