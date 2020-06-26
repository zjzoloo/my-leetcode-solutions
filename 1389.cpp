/*
	Author: Zoljargal Gantumur
	Runtime: 4 ms, faster than 63.86% of C++ online submissions
	Memory Usage: 8.6 MB, less than 26.49% of C++ online submissions
*/
class Solution {
public:
    vector<int> createTargetArray(vector<int>& nums, vector<int>& index) {
        vector<int> ans;
        ans.reserve(nums.size());
        for(int i=0; i<index.size(); i++){
            ans.insert(ans.begin() + index[i], nums[i]);
        }
        return ans;
    }
};
