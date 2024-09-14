class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:

        def convert_to_binary(num):
            if num == 0:
                return str(num)
            binary_num = []
            while num:
                binary_num.insert(0, str(num % 2 ))
                num = num // 2 
            return "".join(binary_num)

        startbin = convert_to_binary(start)
        goalbin = convert_to_binary(goal)

        
        if len(startbin) > len(goalbin):
            while len(startbin) != len(goalbin):
                goalbin = str(0) + goalbin
        else:
            while len(goalbin) != len(startbin):
                startbin = str(0) + startbin
        
        min_steps = 0
        for i, j in zip(startbin, goalbin):
            if i != j:
                min_steps += 1
        return min_steps

        
