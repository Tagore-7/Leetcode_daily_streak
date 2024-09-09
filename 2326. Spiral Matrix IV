# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[0] * n for _ in range(m)]
        visited = [[False] * n for _ in range(m)]
        directions = [(0, 1), (1,0), (0, -1), (-1, 0)]
        r, c = 0, 0
        di = 0

        def check(r, c, di):
            visited[r][c] = True
            dr, dc = directions[di]
            newR, newC = r + dr , c + dc
            if 0 <= newR < m and 0 <= newC < n and not visited[newR][newC]:
                r, c = newR, newC
            else:
                di = (di + 1) % 4
                tr, tc = directions[di]
                r += tr
                c +=  tc 
            return r, c , di

        for i in range(m * n):
            if head:
                matrix[r][c] = head.val
                head = head.next 
                r, c, di = check(r, c, di)
            else:
                matrix[r][c] = -1
                r, c, di = check(r, c, di)
        return matrix
            
        
        
