/*
	Author: Zoljargal Gantumur
	Runtime: 4 ms, faster than 50.76% of C++ online submissions
	Memory Usage: 6.2 MB, less than 72.49% of C++ online submissions
*/

class Solution {
public:
    string freqAlphabets(string s) {
            string ans="";
            int n=s.length();
            int i=0;
            while(i<n){
                if((n-i)>2 && s[i+2]=='#'){
                    ans+=(char)(((s[i]-48)*10+(s[i+1]-48))+96);
                    i+=2;
                } else {
                    ans+=(char)((s[i]-48)+96);

                }
                i++;
            }
            return ans;
    }
};
