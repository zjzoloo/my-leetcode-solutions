/*
	Author: Zoljargal Gantumur
	Runtime: 0 ms, faster than 100.00% of C++ online submissions
	Memory Usage: 6.1 MB, less than 43.43% of C++ online submissions
*/

class Solution {
public:
    int maximum69Number (int num) {
        string s = to_string(num);
        for (int i=0; i<s.size(); i++){
            if(s[i]=='9') continue;
            else s[i]='9';
            break;
        }
        return stoi(s);
    }
};
