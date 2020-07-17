/*
	Author: Zoljargal Gantumur
	Runtime: 72 ms
	Memory Usage: 19.8 MB
	
	Given an array nums of n integers, are there elements a, b, c in nums 
	such that a + b + c = 0? Find all unique triplets in the array which 
	gives the sum of zero.
	
	Given array nums = [-1, 0, 1, 2, -1, -4],

	A solution set is:
	[
	  [-1, 0, 1],
	  [-1, -1, 2]
	]
*/

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        int x = nums.size();
        if (x<3) return {};
        vector<vector<int>> ans;
        sort(nums.begin(), nums.end());
        for (int i=0; i<x-2; ++i){
            if(i==0 || nums[i] != nums[i-1]){
                int j=i+1;
                int k=x-1;
                while(j<k){
                    int sum = nums[i] + nums[j] + nums[k];
                    if (sum==0){
                        ans.push_back({nums[i], nums[j], nums[k]});
                        while(j<k && nums[j] == nums[j+1]) j++;
                        while(j<k && nums[k] == nums[k-1]) k--;
                        j++; 
                        k--;
                    }
                    else if (sum > 0) k--;
                    else j++;
                }
            }
        }
        return ans;
    }
};
