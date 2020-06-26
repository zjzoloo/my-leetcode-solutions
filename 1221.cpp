/*
	Author: Zoljargal Gantumur
	Runtime: 0 ms, faster than 100.00% of C++ online submissions
	Memory Usage: 6.4 MB, less than 12.45% of C++ online submissions
*/ 

class Solution {
public:
    int balancedStringSplit(string s) {
        int a = 0;
        int ans = 0;
        for(int i=0; i<s.size(); i++){
            if(s[i] == 'R'){
                ans++;
            }else{
                ans--;
            }
            if (ans==0){
                a++;
            }
        }
        return a;
    }
};
