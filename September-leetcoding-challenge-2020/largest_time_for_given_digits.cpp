/*
	Runtime: 4 ms
	Memory Usage: 9.6 MB
	
	Given an array of 4 digits, return the largest 24 hour time that can be made.
	The smallest 24 hour time is 00:00, and the largest is 23:59.  
	Starting from 00:00, a time is larger if more time has elapsed since midnight.

	Return the answer as a string of length 5.  If no valid time can be made, return an empty string.

	Input: A = [1,2,3,4]
	Output: "23:41"

	Input: A = [5,5,5,5]
	Output: ""

	Input: A = [0,0,0,0]
	Output: "00:00"

	Input: A = [0,0,1,0]
	Output: "10:00"
*/
class Solution {
public:
    string largestTimeFromDigits(vector<int>& arr) {
        string ans;
        for(int i = 0; i < 4; ++i){
            for(int j = 0; j < 4; ++j){
                for(int k = 0; k < 4; ++k){
                    if(i == j || j == k || k == i) continue;
                    string hour = to_string(arr[i]) + to_string(arr[j]);
                    string min = to_string(arr[k]) + to_string(arr[6-i-j-k]);
                    string time = hour + ":" + min;
                    if(hour < "24" && min < "60" && time > ans) ans = time;
                }
            }
        }
        return ans;
    }
};
