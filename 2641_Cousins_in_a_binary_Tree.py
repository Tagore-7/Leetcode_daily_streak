#Given the root of a binary tree, replace the value of each node in the tree with the sum of all its cousins' values.
#
#Two nodes of a binary tree are cousins if they have the same depth with different parents.
#
#Return the root of the modified tree.
#
#Note that the depth of a node is the number of edges in the path from the root node to it.
#
# 
#
#Example 1:
#
#
#Input: root = [5,4,9,1,10,null,7]
#Output: [0,0,0,7,7,null,11]
#Explanation: The diagram above shows the initial binary tree and the binary tree after changing the value of each node.
#- Node with value 5 does not have any cousins so its sum is 0.
#- Node with value 4 does not have any cousins so its sum is 0.
#- Node with value 9 does not have any cousins so its sum is 0.
#- Node with value 1 has a cousin with value 7 so its sum is 7.
#- Node with value 10 has a cousin with value 7 so its sum is 7.
#- Node with value 7 has cousins with values 1 and 10 so its sum is 11.
#Example 2:
#
#
#Input: root = [3,1,2]
#Output: [0,0,0]
#Explanation: The diagram above shows the initial binary tree and the binary tree after changing the value of each node.
#- Node with value 3 does not have any cousins so its sum is 0.
#- Node with value 1 does not have any cousins so its sum is 0.
#- Node with value 2 does not have any cousins so its sum is 0.
# 
#
#Constraints:
#
#The number of nodes in the tree is in the range [1, 105].
#1 <= Node.val <= 104
#
class TreeNode:
    def __init__(self, val):
        self.val = val 
        self.left = None
        self.right = None 

class Solution:
    def replaceValueinTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([root])

        level_sum = []
        while queue:
            cur_sum  = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                cur_sum += node.val 
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level_sum.append(cur_sum)

        queue = deque([(root, root.val)])
        level = 0
        while queue:
            for _ in range(len(queue)):
                node, val = queue.popleft()
                node.val = level_sum[level] - val 
                child_sum = 0

                if node.left:
                    child_sum += node.left.val
                if node.right:
                    child_right += node.right.val

                if node.left:
                    queue.append((root.left, child_sum))
                if node.right:
                    queue.appemd((root.right, child_sum))

            level += 1

        return root 




