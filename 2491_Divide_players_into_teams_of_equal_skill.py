#You are given a positive integer array skill of even length n where skill[i] denotes the skill of the ith player. Divide the players into n / 2 teams of size 2 such that the total skill of each team is equal.
#
#The chemistry of a team is equal to the product of the skills of the players on that team.
#
#Return the sum of the chemistry of all the teams, or return -1 if there is no way to divide the players into teams such that the total skill of each team is equal.
#
# 
#
#Example 1:
#
#Input: skill = [3,2,5,1,3,4]
#Output: 22
#Explanation: 
#Divide the players into the following teams: (1, 5), (2, 4), (3, 3), where each team has a total skill of 6.
#The sum of the chemistry of all the teams is: 1 * 5 + 2 * 4 + 3 * 3 = 5 + 8 + 9 = 22.
#Example 2:
#
#Input: skill = [3,4]
#Output: 12
#Explanation: 
#The two players form a team with a total skill of 7.
#The chemistry of the team is 3 * 4 = 12.
#Example 3:
#
#Input: skill = [1,1,2,3]
#Output: -1
#Explanation: 
#There is no way to divide the players into teams such that the total skill of each team is equal.
# 
#
#Constraints:
#
#2 <= skill.length <= 105
#skill.length is even.
#1 <= skill[i] <= 1000

#my first solution without any hints 
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        if len(skill) == 2:
            return skill[0] * skill[1]
        skill.sort()
        firstsum  =  skill[0] + skill[-1]
        teams = [skill[0] * skill[-1]]
        i = 1
        j = len(skill) - 2
        while skill[i] + skill[j] == firstsum:
            teams.append(skill[i] * skill[j])
            j -= 1
            i += 1
            if i > j:
                break
        if i > j:
            return sum(teams)
        return -1

# leetcode hashmap solution
class solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skillsum = sum(skill)
        n = len(skill)
        skillfreq = [0] * 1001

        for player in skill:
            skillfreq[player] += 1

        if skillsum % (n // 2) == 0:
            return -1 
        
        targetteamskill = skillsum // (n // 2)
        totalchem = 0

        for playerskill in skill:
            partnerskill = targetteamskill - playerskill

            if skillfreq[partnerskill] == 0:
                return -1 
            
            totalchem += playerskill * partnerskill 
            skillfreq[partnerskill] -= 1

        return totalchem // 2
