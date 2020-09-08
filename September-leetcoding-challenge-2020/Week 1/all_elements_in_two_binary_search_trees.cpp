/*
	Runtime: 228 ms
	Memory Usage: 84.6 MB
	
	Given two binary search trees root1 and root2.

	Return a list containing all the integers from both trees sorted in ascending order.

	Input: root1 = [2,1,4], root2 = [1,0,3]
	Output: [0,1,1,2,3,4]

	Input: root1 = [0,-10,10], root2 = [5,1,7,0,2]
	Output: [-10,0,0,1,2,5,7,10]

	Input: root1 = [], root2 = [5,1,7,0,2]
	Output: [0,1,2,5,7]

	Input: root1 = [0,-10,10], root2 = []
	Output: [-10,0,10]

	Input: root1 = [1,null,8], root2 = [8,1]
	Output: [1,1,8,8]
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
    vector<int> getAllElements(TreeNode* root1, TreeNode* root2) {
        stack<TreeNode *> S1, S2;
        vector<int> ans;
        while(root1 || root2 || !S1.empty() || !S2.empty()){
            while(root1){
                S1.push(root1);
                root1 = root1->left;
            }
            while(root2){
                S2.push(root2);
                root2 = root2->left;
            }
            if(S2.empty() || (!S1.empty() && S1.top()->val <= S2.top()->val)){
                root1 = S1.top();
                S1.pop();
                ans.push_back(root1->val);
                root1 = root1->right;
            } else {
                root2 = S2.top();
                S2.pop();
                ans.push_back(root2->val);
                root2 = root2->right;
            }
        }
        return ans;
    }
};
