# Author: Zoljargal Gantumur
# Runtime: 68ms
# Memory Usage: 14.2MB

# Given binary tree [3,9,20,null,null,15,7],
#    3
#   / \
#  9  20
#    /  \
#   15   7

#return its bottom-up level order traversal as:
# [
#  [15,7],
#  [9,20],
#  [3]
# ]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        ans = []
        if root==None: return ans
        Q = []
        Q.append(root)
        while len(Q) != 0:
            nodes = []
            for i in range(len(Q)):
                node = Q.pop(0)
                nodes.append(node.val)
                if(node.left != None): Q.append(node.left);
                if(node.right != None): Q.append(node.right);
            ans.insert(0,nodes);
        return ans;
