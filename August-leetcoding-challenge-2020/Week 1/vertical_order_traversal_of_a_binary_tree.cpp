/*
	Runtime: 4 ms
	Memory Usage: 12.2 MB
	
	Given a binary tree, return the vertical order traversal of its nodes values.
	For each node at position (X, Y), its left and right children respectively will be at positions (X-1, Y-1) and (X+1, Y-1).
	Running a vertical line from X = -infinity to X = +infinity, whenever the vertical line touches some nodes, 
	we report the values of the nodes in order from top to bottom (decreasing Y coordinates).
	If two nodes have the same position, then the value of the node that is reported first is the value that is smaller.
	Return an list of non-empty reports in order of X coordinate.  Every report will have a list of values of nodes.

	Input: [3,9,20,null,null,15,7]
	Output: [[9],[3,15],[20],[7]]
	Explanation: 
	Without loss of generality, we can assume the root node is at position (0, 0):
	Then, the node with value 9 occurs at position (-1, -1);
	The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2);
	The node with value 20 occurs at position (1, -1);
	The node with value 7 occurs at position (2, -2).

	Input: [1,2,3,4,5,6,7]
	Output: [[4],[2],[1,5,6],[3],[7]]
	Explanation: 
	The node with value 5 and the node with value 6 have the same position according to the given scheme.
	However, in the report "[1,5,6]", the node value of 5 comes first since 5 is smaller than 6.
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
    struct trp {int x, y, val;};                                                                 // Instead of using a pair of pairs, it's easier to use a struct of trp (triples)
    vector <trp> cord;                                                                           // This will store coordinates of a node and its value
    void dfs(TreeNode *node, int x, int y) {                                                     // dfs with coordinates
        cord.push_back({x, y, node->val});                                                       // Push coordinates and value
        if (node->left)  dfs(node->left , x - 1, y - 1);                                         // If there is a left child, then from the problem statement, its coordinates are (x - 1, y - 1)
        if (node->right) dfs(node->right, x + 1, y - 1);                                         // If there is a right child, then from the problem statement, its coordinates are (x + 1, y - 1)
    }
    vector<vector<int>> verticalTraversal(TreeNode* root) {
        vector<vector<int>> ans;                                                                 // Our output
        dfs(root, 0, 0);                                                                         // 'Without loss of generality, we can assume the root node is at position (0, 0):'
        sort(cord.begin(), cord.end(), [](trp a, trp b){return a.x == b.x ? a.y == b.y ? a.val < b.val : a.y > b. y : a.x < b.x;}); // Tricky part, see 'P.s.'
        for(int i=0; i<cord.size();) {
            vector <int> aux;                                                                    // The output should be a vector of vectors, so let's create an auxiliary vector which will store values with the same x coordinates
            do aux.push_back(cord[i++].val); while (i<cord.size() and cord[i].x == cord[i-1].x); // While x coordinate is the same, we push this value
            ans.push_back(aux);                                                                  // Push the aux vector to our answer
        }
        return ans;                                                                              // return answer
    }
};
