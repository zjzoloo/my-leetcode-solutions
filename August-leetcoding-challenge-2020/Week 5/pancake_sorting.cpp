/*
	Runtime: 4 ms
	Memory Usage: 11.4 MB
	
	Given an array of integers arr, we need to sort the array performing a series of pancake flips.
	
	In one pancake flip we do the following steps:
	Choose an integer k where 1 <= k <= arr.length.
	Reverse the sub-array arr[1...k].
	For example, if arr = [3,2,1,4] and we performed a pancake flip choosing k = 3, we reverse the sub-array [3,2,1], 
	so arr = [1,2,3,4] after the pancake flip at k = 3.

	Return an array of the k-values of the pancake flips that should be performed in order to sort arr. 
	Any valid answer that sorts the array within 10 * arr.length flips will be judged as correct.

	Input: arr = [3,2,4,1]
	Output: [4,2,4,3]
	Explanation: 
	We perform 4 pancake flips, with k values 4, 2, 4, and 3.
	Starting state: arr = [3, 2, 4, 1]
	After 1st flip (k = 4): arr = [1, 4, 2, 3]
	After 2nd flip (k = 2): arr = [4, 1, 2, 3]
	After 3rd flip (k = 4): arr = [3, 2, 1, 4]
	After 4th flip (k = 3): arr = [1, 2, 3, 4], which is sorted.
	Notice that we return an array of the chosen k values of the pancake flips.


	Input: arr = [1,2,3]
	Output: []
	Explanation: The input is already sorted, so there is no need to flip anything.
	Note that other answers, such as [3, 3], would also be accepted.
*/
class Solution {
    void flip(vector<int>& arr, int idx){
        for(int i = 0; i <= idx/2; ++i){
            int tmp = arr[i];
            arr[i] = arr[idx-i];
            arr[idx-i] = tmp;
        }
    }
public:
    vector<int> pancakeSort(vector<int>& arr) {
        vector<int> ans;
        for(int i = arr.size()-1; i > 0; --i){
            for(int j = 1; j <= i; ++j){
                if(arr[j] == i+1){
                    flip(arr, j);
                    ans.push_back(j+1);
                    break;
                }
            }
            flip(arr, i);
            ans.push_back(i+1);
        }
        return ans;
    }
};
