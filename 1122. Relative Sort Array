class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1Map = Counter(arr1)
        ans = []
        for num in arr2:
            if num in arr1Map:
                ans.extend([num] * arr1Map[num])
                del arr1Map[num]
        rem_elements = sorted(arr1Map.elements())
        ans.extend(rem_elements)
        return ans
