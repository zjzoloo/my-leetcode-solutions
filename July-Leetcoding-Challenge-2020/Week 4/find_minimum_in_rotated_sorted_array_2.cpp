/*
	Author: Zoljargal Gantumur
	Runtime: 8 ms
	Memory Usage: 12.3 MB
	
	Find the minimum element.
	The array may contain duplicates.

	Example 1:
	Input: [1,3,5]
	Output: 1
	
	Example 2:
	Input: [2,2,2,0,1]
	Output: 0
*/

class Solution {
public:
    int findMin(vector<int>& nums) {
        return *std::min_element(nums.begin(), nums.end());
    }
};
