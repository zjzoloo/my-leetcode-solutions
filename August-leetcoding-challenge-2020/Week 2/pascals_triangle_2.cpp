/*
	Runtime: 0 ms
	Memory Usage: 6.2 MB
	
	Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
	Note that the row index starts from 0.

			  1
			 / \
			1   1
		   / \ / \
		  1   2   1
		 / \ / \ / \
		1   3   3   1
	   / \ / \ / \ / \
	  1   4   6   4   1

	Input: 3
	Output: [1,3,3,1]
*/

class Solution {
public:
    vector<int> getRow(int rowIndex) {      
        vector<int> row(rowIndex + 1);
        row[0] = 1;
        int prev, sum;
        for(int i = 1; i <= rowIndex; ++i){
            prev = 1;
            for(int j = 1; j < i; ++j){
                sum = prev + row[j];
                prev = row[j];
                row[j] = sum;
            }
            row[i] = 1;
        }
        return row;
    }
};
