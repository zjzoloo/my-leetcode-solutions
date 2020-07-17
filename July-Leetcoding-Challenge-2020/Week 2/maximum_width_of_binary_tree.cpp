/*
	Author: Zoljargal Gantumur
	Runtime: 20 ms
	Memory Usage: 16.5 MB
	
	Given a binary tree, write a function to get the maximum width of the given tree. 
	The maximum width of a tree is the maximum width among all levels.
	The width of one level is defined as the length between the end-nodes 
	(the leftmost and right most non-null nodes in the level, where the null nodes 
	between the end-nodes are also counted into the length calculation.

	It is guaranteed that the answer will in the range of 32-bit signed integer.
	
	Input: 
			   1
			 /   \
			3     2
		   / \     \  
		  5   3     9 

	Output: 4
	Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
	
	Input: 
			  1
			 /  
			3    
		   / \       
		  5   3     

	Output: 2
	Explanation: The maximum width existing in the third level with the length 2 (5,3).
	
		Input: 
			  1
			 / \
			3   2 
		   /        
		  5      

	Output: 2
	Explanation: The maximum width existing in the second level with the length 2 (3,2).
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
public:
    int widthOfBinaryTree(TreeNode* root) {
        if(!root) return 0;
        int ans = 1;
        queue<pair<TreeNode*, int>> Q;
        Q.push({root, 0});
        while(!Q.empty()){
            int count = Q.size();
            int startIndex = Q.front().second;
            int endIndex = Q.back().second;
            ans = max(ans, endIndex-startIndex+1);
            for(int i=0; i<count; ++i){
                pair<TreeNode*, int> p = Q.front();
                int idx = p.second - startIndex;
                Q.pop();
                if(p.first->left) Q.push({p.first->left, 2*idx+1});
                if(p.first->right) Q.push({p.first->right, 2*idx+2});
            }
        }
        return ans;
    }
};
