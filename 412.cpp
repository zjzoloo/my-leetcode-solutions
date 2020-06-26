/*
	Author: Zoljargal Gantumur
	Runtime: 0 ms, faster than 100.00% of C++ online submissions
	Memory Usage: 7.3 MB, less than 93.18% of C++ online submissions
*/

class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string> ans;
        ans.reserve(n);
        for(int i=1; i<=n; i++){
            if(i%3 == 0){
                if(i%5 == 0){
                    ans.push_back("FizzBuzz");
                } else {
                    ans.push_back("Fizz");
                }
                
            } else if (i%5 == 0){
                if(i%3 == 0){
                    ans.push_back("FizzBuzz");
                } else {
                    ans.push_back("Buzz");
                }
            } else {
                ans.push_back(to_string(i));
            }
        }
        return ans;
    }
};
