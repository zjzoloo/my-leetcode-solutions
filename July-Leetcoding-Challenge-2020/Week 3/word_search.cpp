/*
	Author: Zoljargal Gantumur
	Runtime: 60 ms
	Memory Usage: 11.4 MB
	
	Given a 2D board and a word, find if the word exists in the grid.
	The word can be constructed from letters of sequentially adjacent cell, 
	where "adjacent" cells are those horizontally or vertically neighboring. 
	The same letter cell may not be used more than once.

	Example:
	board =
	[
	  ['A','B','C','E'],
	  ['S','F','C','S'],
	  ['A','D','E','E']
	]

	Given word = "ABCCED", return true.
	Given word = "SEE", return true.
	Given word = "ABCB", return false.
*/
class Solution {
    bool search(vector<vector<char>>& board, int i, int j, string& word, int idx){
        if(idx == word.length() - 1) return true;
        board[i][j] -= 65;
        if(i > 0 && board[i-1][j] == word[idx+1] && search(board, i-1, j, word, idx+1)){
            return true;
        }
        if(j > 0 && board[i][j-1] == word[idx+1] && search(board, i, j-1, word, idx+1)){
            return true;
        }
        if(i < board.size()-1 && board[i+1][j] == word[idx+1] && search(board, i+1, j, word, idx+1)){
            return true;
        }
        if(j < board[0].size()-1 && board[i][j+1] == word[idx+1] && search(board, i, j+1, word, idx+1)){
            return true;
        }
        board[i][j] += 65;
        return false;
    }
public:
    bool exist(vector<vector<char>>& board, string word) {
        int row = board.size();
        int col = board[0].size();
        vector<vector<bool>> visited(row, vector<bool>(col, false));
        for(int i=0; i<row; ++i){
            for(int j=0; j<col; ++j){
                if(board[i][j] == word[0] && search(board, i, j, word, 0)) {
                    return true;
                }
            }
        }
        return false;
    }
};
