/*
	Author: Zoljargal Gantumur
	Runtime: 48 ms
	Memory Usage: 14.3 MB
	
	There are a total of n courses you have to take, labeled from 0 to n-1.
	Some courses may have prerequisites, for example to take course 0 you have to first take course 1, 
	which is expressed as a pair: [0,1]

	Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you 
	should take to finish all courses.
	There may be multiple correct orders, you just need to return one of them. 
	If it is impossible to finish all courses, return an empty array.

	Example 1:
	Input: 2, [[1,0]] 
	Output: [0,1]
	Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
				 course 0. So the correct course order is [0,1] .

	Example 2:
	Input: 4, [[1,0],[2,0],[3,1],[3,2]]
	Output: [0,1,2,3] or [0,2,1,3]
	Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both     
				 courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. 
				 So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
*/
class Solution {
    bool dfs(int u, vector<vector<int>>& adj, vector<int>& stack, vector<int>& visited){
        visited[u] = 1;
        for(int v : adj[u]){
            if(visited[v] == 1){
                return true;
            } 
            if(visited[v] == 0 && dfs(v, adj, stack, visited)){
                return true;
            }
        }
        visited[u] = 2;
        stack.push_back(u);
        return false;
    }
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> adj(numCourses);
        for(vector<int>& courses: prerequisites){
            adj[courses[1]].push_back(courses[0]);
        }
        
        vector<int> stack;
        vector<int> visited(numCourses, 0);
        for(int i=0; i<numCourses; ++i){
            if(visited[i] == 0 && dfs(i, adj, stack, visited)){
                return {};
            }
        }
        reverse(stack.begin(), stack.end());
        return stack;
    }
};
