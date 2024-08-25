# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def method(self, root, node_value):
        if root == None:
            return 
        self.method(root.left,node_value)
        self.method(root.right, node_value)
        node_value.append(root.val)

        return node_value

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        node_values = []
        self.method(root,node_values)
        return node_values
          
