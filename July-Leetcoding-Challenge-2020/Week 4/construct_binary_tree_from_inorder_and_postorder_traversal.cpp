/*
	Author: Zoljargal Gantumur
	Runtime: 48 ms
	Memory Usage: 24.3 MB
	
	Given inorder and postorder traversal of a tree, construct the binary tree.

	Note:
	You may assume that duplicates do not exist in the tree.

	For example, given
	inorder = [9,3,15,20,7]
	postorder = [9,15,7,20,3]
	
	Return the following binary tree:
		3
	   / \
	  9  20
		/  \
	   15   7
*/

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
    TreeNode* rec_func(vector<int>& inorder, int in_first, int in_end, vector<int>& postorder, int post_first, int post_end) {
        if(in_first >= in_end || post_first >= post_end) return nullptr;
        TreeNode *root = new TreeNode(postorder[post_end-1]);
        auto itera = find(inorder.begin() + in_first, inorder.begin() + in_end, postorder[post_end-1]);
        int diff = itera - inorder.begin() - in_first;
        root->left = rec_func(inorder, in_first, in_first + diff, postorder, post_first, post_first + diff);
        root->right = rec_func(inorder, in_first + diff + 1, in_end, postorder, post_first + diff, post_end-1);
        
        return root;
    }
public:
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        int n = inorder.size();
        if(n == 0) return nullptr;
        
        return rec_func(inorder, 0, n, postorder, 0, n);
    }
};
