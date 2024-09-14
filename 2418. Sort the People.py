class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        Map = dict(zip(heights, names))
        sorted_heights = sorted(heights, reverse = True)
        sorted_names = [Map[height] for height in sorted_heights]
        return sorted_names
