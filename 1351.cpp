/*
	Author: Zoljargal Gantumur
	Runtime: 24 ms, faster than 88.85% of C++ online submissions
	Memory Usage: 10.6 MB, less than 54.54% of C++ online submissions
*/ 

class Solution {
public:
    int countNegatives(vector<vector<int>>& grid) {
        std::ios_base::sync_with_stdio(false);
        cin.tie(NULL);
        int count=0;
        int m=grid.size();
        int n=grid[0].size();
        for(int i=0;i<m;i++)
        {
            for(int j=n-1;j>=0;j--)
            {
                if(grid[i][j]>=0)
                    break;
                 count++;
            }
        }
        return count;
    }
};
