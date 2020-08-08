/*
	Author: Zoljargal Gantumur
	Runtime: 8 ms
	Memory Usage: 10.5 MB
	
	Given a directed acyclic graph of N nodes. Find all possible paths from node 0 to node N-1, and return them in any order.
	The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.  
	graph[i] is a list of all nodes j for which the edge (i, j) exists.

	Example:
	Input: [[1,2],[3],[3],[]]
	Output: [[0,1,3],[0,2,3]]
	Explanation: The graph looks like this:
	0--->1
	|    |
	v    v
	2--->3
	There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
*/
class Solution {
    void dfs(vector<vector<int>>& graph, vector<vector<int>>& ans, vector<int>& path, int a){
        path.push_back(a);
        if(a == graph.size()-1){
            ans.push_back(path);
        } 
        else {
            for(int i: graph[a]){
                dfs(graph, ans, path, i);
            } 
        }
        path.pop_back();
    }
public:
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
        vector<vector<int>> ans;
        vector<int> path;
        dfs(graph, ans, path, 0);
        return ans;
    }
};
