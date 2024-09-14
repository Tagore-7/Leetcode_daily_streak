class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        Map = Counter(arr)
        klist = []
        i = 1
        for string in Map.items():
            if string[1] == 1:
                if i == k:
                    return string[0]
                i += 1
        return ""
