/*
	Author: Zoljargal Gantumur
	Runtime: 4 ms, faster than 86.94% of C++ online submissions
	Memory Usage: 9 MB, less than 83.31% of C++ online submissions
*/

class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        vector<bool> ans;
        ans.reserve(candies.size());
        int maxEl = *max_element(candies.begin(), candies.end());
        for(int n : candies){
            if(n + extraCandies >= maxEl){
                ans.push_back(true);
            } else {
                ans.push_back(false);
            }
        }
        return ans;
    }
};

