/*
	Author: Zoljargal Gantumur
	Runtime: 4 ms, faster than 93.14% of C++ online submissions
	Memory Usage: 8.7 MB, less than 40.00% of C++ online submissions
*/

class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        vector<int> ans;
        int sum =0;
        for(int num: nums){
            sum+=num;
            ans.push_back(sum);
        }
        return ans;
    }
};
