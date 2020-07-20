# Author: Zoljargal Gantumur
# Runtime: 24 ms
# Memory Usage: 14 MB

# Given two binary trees, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical 
# and the nodes have the same value.

#Input:     1         1
#          / \       / \
#         2   3     2   3
#
#        [1,2,3],   [1,2,3]
#
#Output: true

#Input:     1         1
#          /           \
#         2             2
#
#        [1,2],     [1,null,2]
#
#Output: false

#Input:     1         1
#          / \       / \
#         2   1     1   2
#
#        [1,2,1],   [1,1,2]
#
#Output: false

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not q or not p:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.right, q.right) and \
               self.isSameTree(p.left, q.left)
