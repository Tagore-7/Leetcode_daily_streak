class Solution:
    def judgeCircle(self, moves: str) -> bool:
        rightscore, leftscore = 0, 0
        for char in moves:
            if char == "R":
                rightscore += 1
            elif char == 'L':
                rightscore -= 1
            elif char == 'U':
                leftscore += 1
            else:
                leftscore -= 1
        if leftscore == 0 and rightscore ==0:
            return True
        return False
        
