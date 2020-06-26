/*
	Author: Zoljargal Gantumur
	Runtime: 8 ms, faster than 95.25% of C++ online submissions
	Memory Usage: 9.9 MB, less than 100.00% of C++ online submissions
*/

class Solution {
public:
    vector<int> shuffle(vector<int>& nums, int n) {
        vector<int> ans;
        ans.reserve(nums.size());
        for(int i=0; i<n; i++){
            ans.push_back(nums[i]);
            ans.push_back(nums[i+n]);
        }
        return ans;
    }
};
