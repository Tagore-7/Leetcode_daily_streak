# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.sorted_array = []
        self.inorder_traverse(root)
        return self.sorted_array_to_bst(0, len(self.sorted_array) - 1)

    def inorder_traverse(self, root: TreeNode) -> None:
        if not root:
            return
        self.inorder_traverse(root.left)
        self.sorted_array.append(root)
        self.inorder_traverse(root.right)

    def sorted_array_to_bst(self, start: int, end: int) -> TreeNode:
        if start > end:
            return None
        mid = (start +  end) // 2
        root = self.sorted_array[mid]
        root.left = self.sorted_array_to_bst(start, mid - 1)
        root.right = self.sorted_array_to_bst(mid +1, end)
        return root
