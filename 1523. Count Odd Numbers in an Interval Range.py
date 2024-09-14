class Solution:
    def countOdds(self, low: int, high: int) -> int:
        high_odds =  (high + 1) // 2
        low_odds = low // 2
        return high_odds - low_odds
