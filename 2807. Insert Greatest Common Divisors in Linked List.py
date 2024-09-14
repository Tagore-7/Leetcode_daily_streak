# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def gcd(a, b):
            if a == 0:
                return b 
            if b == 0:
                return a
            if a == b:
                return a
            if a > b:
                return gcd(a - b, b)
            return gcd(a, b - a)
        temp = head
        while head.next:
            a = head.val 
            b = head.next.val 
            gcdvalnode = ListNode(gcd(a,b))
            tmp = head.next
            gcdvalnode.next = head.next
            head.next = gcdvalnode
            gcdvalnode.next = tmp
            head = head.next.next
        return temp
