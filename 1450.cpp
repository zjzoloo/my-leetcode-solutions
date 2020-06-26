/*
	Author: Zoljargal Gantumur
	Runtime: 4 ms, faster than 90.10% of C++ online submissions
	Memory Usage: 11.1 MB, less than 42.70% of C++ online submissions
*/

class Solution {
public:
    int busyStudent(vector<int>& startTime, vector<int>& endTime, int queryTime) {
        int count = 0;
        for(int i=0; i<startTime.size(); i++){
            if(startTime[i]<=queryTime && queryTime<=endTime[i]){
                count++;
            }
        }
        return count;
    }
};
