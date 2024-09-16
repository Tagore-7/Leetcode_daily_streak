# Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.
 

#Example 1:
#
#Input: timePoints = ["23:59","00:00"]
#Output: 1
#Example 2:
#
#Input: timePoints = ["00:00","23:59","00:00"]
#Output: 0
# 
#
#Constraints:
#
#2 <= timePoints.length <= 2 * 104
#timePoints[i] is in the format "HH:MM".
#


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        def conver_to_min(s):
            return int(s[0:2])  * 60 + int(s[3:]) 
        
        timeMinutes = sorted([conver_to_min(time) for time in timePoints])
        min_min = float("Inf")

        for i in range(len(timeMinutes)-1):
            min_min = min(min_min, timeMinutes[i + 1] - timeMinutes[i])
        cir_diff = (24 * 60 ) - timeMinutes[-1] +  timeMinutes[0]
        min_min = min(cir_diff, min_min)
        return min_min


