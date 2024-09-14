class Solution:
    def minimumPushes(self, word: str) -> int:
        count = 2
        score = 0
        Map = Counter(word)
        for key, value in Map.most_common():
            if count <= 9:
                score += value * 1  
                count += 1
            elif count > 9 and count <= 17:
                score +=  value * 2
                count += 1 
            elif count > 17 and count <= 25:
                score += value * 3 
                count += 1
            else:
                score += value * 4
                count += 1
        return score
