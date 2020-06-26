/*
	Author: Zoljargal Gantumur
	Runtime: 0 ms, faster than 100.00% of C++ online submissions
	Memory Usage: 6.1 MB, less than 92.04% of C++ online submissions
*/

class Solution {
public:
    int numJewelsInStones(string J, string S) {
        int count = 0;
        int lenJ, lenS;
        lenJ = J.size();
        lenS = S.size();
        for(int i=0; i<lenS; i++){
            for(int j=0; j<lenJ; j++){
                if(S[i] == J[j]){
                    count++;
                }
            }
        }
        return count;
    }
};
