#Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in any order.
#
#The test cases are generated such that the output values fit in a 32-bit integer and the number of different results does not exceed 104.
#
# 
#
#Example 1:
#
#Input: expression = "2-1-1"
#Output: [0,2]
#Explanation:
#((2-1)-1) = 0 
#(2-(1-1)) = 2
#Example 2:
#
#Input: expression = "2*3-4*5"
#Output: [-34,-14,-10,-10,10]
#Explanation:
#(2*(3-(4*5))) = -34 
#((2*3)-(4*5)) = -14 
#((2*(3-4))*5) = -10 
#(2*((3-4)*5)) = -10 
#(((2*3)-4)*5) = 10
# 
#
#Constraints:
#
#1 <= expression.length <= 20
#expression consists of digits and the operator '+', '-', and '*'.
#All the integer values in the input expression are in the range [0, 99].
#The integer values in the input expression do not have a leading '-' or '+' denoting the sign.

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        ans = []
        if not expression:
            return  ans
        if len(expression) == 1:
            return [int(expression)]
        if len(expression) == 2 and expression[0].isdigit():
            return [int(expression)]
        for i, c in enumerate(expression):
            if c.isdigit():
                continue
            left = self.diffWaysToCompute(expression[:i])
            right = self.diffWaysToComputer(expression[i + 1:])

            for lval in left:
                for rval in right:
                    if c == "+":
                        ans.append(lval + rval)
                    elif c == "-":
                        ans,append(lval - rval)
                    else:
                        ans.append(lval * rval)
        return ans
