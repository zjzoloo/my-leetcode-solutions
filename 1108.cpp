/*
	Author: Zoljargal Gantumur
	Runtime: 0 ms, faster than 100.00% of C++ online submissions
	Memory Usage: 6.1 MB, less than 31.33% of C++ online submissions
*/

class Solution {
public:
    string defangIPaddr(string address) {
        string ans="";
        for(char c: address){
            if(c=='.'){
                ans.push_back('[');
                ans.push_back('.');
                ans.push_back(']');
            }else{
                ans+=c;
            }
        }
        return ans;
    }
};
