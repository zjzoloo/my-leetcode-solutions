/*
	Runtime: 20 ms
	Memory Usage: 12.9 MB
	
	Design an Iterator class, which has:

	A constructor that takes a string characters of sorted distinct lowercase English letters and a number 
	combinationLength as arguments.
	A function next() that returns the next combination of length combinationLength in lexicographical order.
	A function hasNext() that returns True if and only if there exists a next combination.
	 

	CombinationIterator iterator = new CombinationIterator("abc", 2); // creates the iterator.

	iterator.next(); // returns "ab"
	iterator.hasNext(); // returns true
	iterator.next(); // returns "ac"
	iterator.hasNext(); // returns true
	iterator.next(); // returns "bc"
	iterator.hasNext(); // returns false
*/

class CombinationIterator {
    queue<string> permutations;
public:
    CombinationIterator(string characters, int combinationLength) {
        string cur;
        dfs(characters, 0, combinationLength, cur);
    }
    
    string next() {
        string res = permutations.front();
        permutations.pop();
        return res;
    }
    
    bool hasNext() {
        return permutations.size() > 0;
    }
    
    void dfs(string& chs, int pos, int len, string& cur){
        if(cur.size() == len) {
            permutations.push(cur);
            return;
        }
        for(int i=pos; i<chs.size(); i++){
            cur += chs[i];
            dfs(chs, i+1, len, cur);
            cur.pop_back();
        }
    }
};

/**
 * Your CombinationIterator object will be instantiated and called as such:
 * CombinationIterator* obj = new CombinationIterator(characters, combinationLength);
 * string param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */
