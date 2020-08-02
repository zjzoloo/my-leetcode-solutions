/*
	Author: Zoljargal Gantumur
	Runtime: 4 ms
	Memory Usage: 6.3 MB
	
	Given two binary strings, return their sum (also a binary string).
	The input strings are both non-empty and contains only characters 1 or 0.

	Example 1:
	Input: a = "11", b = "1"
	Output: "100"
	
	Example 2:
	Input: a = "1010", b = "1011"
	Output: "10101"
*/

class Solution {
public:
    string addBinary(string a, string b) {
        int carry = 0;
        int i = a.length() - 1;
        int j = b.length() - 1;
        string ans;
        while (i >= 0 || j >= 0) {
          int s = (i >= 0 ? a[i--] - '0' : 0) + 
                  (j >= 0 ? b[j--] - '0' : 0) + 
                  carry;
          carry = s >> 1;
          ans += '0' + (s & 1);
        }
        if (carry) ans += '1';
        return {rbegin(ans), rend(ans)};
    }
};
