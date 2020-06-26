/*
	Author: Zoljargal Gantumur
	Runtime: 4 ms, faster than 82.57% of C++ online submissions
	Memory Usage: 8.3 MB, less than 31.52% of C++ online submissions
*/

class Solution {
public:
    int heightChecker(vector<int>& heights) {
        vector<int> v = heights;
        sort(v.begin(), v.end());
        int ans=0;
        for(int i=0; i<v.size(); i++){
            if(v[i]!=heights[i])
                ans++;
        }
        return ans;
    }
};

