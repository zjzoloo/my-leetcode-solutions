/*
	Runtime: 72 ms
	Memory Usage: 7.3 MB
	
	Given a function rand7 which generates a uniform random integer in the range 1 to 7, 
	write a function rand10 which generates a uniform random integer in the range 1 to 10.
	Do NOT use system's Math.random().

	Input: 1
	Output: [7]

	Input: 2
	Output: [8,4]

	Input: 3
	Output: [8,1,10]
*/

// The rand7() API is already defined for you.
// int rand7();
// @return a random integer in the range 1 to 7

class Solution {
public:
    int rand10() {
        int rand40 = 40;
        while(rand40 >= 40){
            rand40 = (rand7() - 1) * 7 + (rand7() - 1);
        }
        return rand40%10+1;
    }
};
