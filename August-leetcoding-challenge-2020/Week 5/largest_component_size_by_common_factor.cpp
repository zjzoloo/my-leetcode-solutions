/*
	Runtime: 256 ms
	Memory Usage: 73.1 MB
	
	Given a non-empty array of unique positive integers A, consider the following graph:
	There are A.length nodes, labelled A[0] to A[A.length - 1];
	There is an edge between A[i] and A[j] if and only if A[i] and A[j] share a common factor greater than 1.
	Return the size of the largest connected component in the graph.

	Input: [4,6,15,35]
	Output: 4

	Input: [20,50,9,63]
	Output: 2

	Input: [2,3,6,7,4,12,21,39]
	Output: 8
*/
class Solution {
    int _find(int  x, vector<int>& parent){
        if(parent[x] == -1)
            return x;
        parent[x] = _find(parent[x], parent);
        return parent[x];
    }
    
    void _union(int x, int y, vector<int>& parent){
        int xp = _find(x, parent);
        int yp = _find(y, parent);
        if (xp != yp)
            parent[yp] = xp;
    }
    
public:
    int largestComponentSize(vector<int>& A) {
        vector<int> parent(100001, -1);
        for(int x: A){
            for(int i=2; i<=sqrt(x); ++i){
                if(x%i==0){
                    _union(i,x,parent);
                    _union(x, x/i, parent);
                }
            }
        }
        int count = 0;
        unordered_map<int, int> cache;
        for(int x: A){
            int xp = _find(x, parent);
            count = max(count, 1+cache[xp]);
            cache[xp] += 1;
        }
        return count;
    }
};
