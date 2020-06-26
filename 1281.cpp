/*
	Author: Zoljargal Gantumur
	Runtime: 0 ms, faster than 100.00% of C++ online submissions
	Memory Usage: 6.1 MB, less than 21.25% of C++ online submissions
*/

class Solution {
public:
    int subtractProductAndSum(int n) {
        int sum=0;
        int product = 1;
        while(n!=0){
            sum += n%10;
            product *= n%10;
            n = n/10;
        }
        return product-sum;
    }
};
