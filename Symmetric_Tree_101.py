"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def isMirror(node_1, node_2):
            if node_1 is None and node_2 is None:
                return True
            if (node_1 is None or node_2 is None):
                return False
            if node_1.val != node_2.val:
                return False
            return isMirror(node_1.left, node_2.right) and isMirror(node_1.right, node_2.left)
        return isMirror(root, root)