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
