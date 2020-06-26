/*
	Author: Zoljargal Gantumur
	Runtime: 8 ms, faster than 95.69% of C++ online submissions
	Memory Usage: 10.6 MB, less than 19.01% of C++ online submissions
*/

class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        vector<int> ans;
        int i, j;
        int count[101] = {0, 0, 0};
        for(i = 0; i < nums.size(); i++) {
            count[nums[i]]++;
        }
        for(i = 1; i < 101; i++) {
            count[i] += count[i - 1];
        }
        for(i = 0; i < nums.size(); i++) {
            if(nums[i] == 0)
                ans.push_back(0);
            else
                ans.push_back(count[nums[i] - 1]);
                
        }
        return ans;
    }
};
