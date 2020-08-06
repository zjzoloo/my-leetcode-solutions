# Author: Zoljargal Gantumur
# Runtime: 48 ms
# Memory Usage: 13.9 MB

# Given a binary tree, return the zigzag level order traversal of its nodes' values. 
# (ie, from left to right, then right to left for the next level and alternate between).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its zigzag level order traversal as:
# [
#   [3],
#   [20,9],
#   [15,7]
# ]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None: return None
        ans = [[]]
        level = 0
        self.func(root, level, ans)
        return ans
    
    def func(self, root, level, ans):
        if root is None: return None
        if len(ans) < level+1: ans.append([])
        ans[level].append(root.val) if level%2==1 else ans[level].insert(0, root.val)   
        self.func(root.right, level+1, ans)
        self.func(root.left, level+1, ans)
