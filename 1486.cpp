/*
	Author: Zoljargal Gantumur
	Runtime: 0 ms, faster than 100.00% of C++ online submissions
	Memory Usage: 6 MB, less than 100.00% of C++ online submissions
*/

class Solution {
public:
    int xorOperation(int n, int start) {
        int ans = start;
        for(int i=1; i<n; i++){
            ans = ans ^ (start+2*i);
        }
        return ans;
    }
};
