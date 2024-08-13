class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        for target in [tops[0], bottoms[0]]:
            missing_top, missing_bottom = 0, 0
            for i, pair in enumerate(zip(tops, bottoms)):
                top, bottom = pair
                if not (top == target or bottom == target):
                    break
                if top != target: missing_top += 1
                if bottom != target: missing_bottom += 1
                if i == len(tops) - 1:
                    return min(missing_top, missing_bottom)
        return -1
