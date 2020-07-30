/*
	Author: Zoljargal Gantumur
	Runtime: 56 ms
	Memory Usage: 13.7 MB
	
	Given a non-empty array of integers, return the k most frequent elements.

	Example 1:
	Input: nums = [1,1,1,2,2,3], k = 2
	Output: [1,2]
	
	Example 2:
	Input: nums = [1], k = 1
	Output: [1]
*/
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        if(k == nums.size()) return nums;
        vector<int> ans;
        auto cmp = [](pair<int, int>& a, pair<int, int>& b){
            return a.second < b.second;
        };
        priority_queue<pair<int, int>, vector<pair<int, int>>, decltype(cmp)> PQ(cmp);

        sort(nums.begin(), nums.end());
        int x = nums[0];
        int n = nums.size();
        int position = 0;

        for(int i = 0; i < n; ++i){
            if(nums[i] != x) {
                PQ.push({x, i-position});
                x = nums[i];
                position = i;
            }
        }
        PQ.push({nums.back(), n-position});

        while(k){
            ans.push_back(PQ.top().first);
            PQ.pop();
            k--;
        }
        return ans;
    }
};
