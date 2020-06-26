/*
	Author: Zoljargal Gantumur
	Runtime: 0 ms, faster than 100.00% of C++ online submissions
	Memory Usage: 6 MB, less than 48.03% of C++ online submissions
*/

class Solution {
public:
    int numberOfSteps (int num) {
        int step = 0;
        while(num!=0){
            if(num%2==0){
                num /= 2;
            } else {
                num -= 1;
            }
            step++;
        }
        return step;
    }
};
