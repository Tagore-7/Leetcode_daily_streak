class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends =  list(range(1, n+1))
        curr_pos = 0

        while n > 1:
            curr_pos = (curr_pos + (k -1)) % n
            # print(curr_pos)
            friends.pop(curr_pos)
            n -= 1

        return friends[0]
