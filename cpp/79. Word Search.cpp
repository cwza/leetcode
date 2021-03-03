#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;
typedef vector<vector<char>> vvc;
typedef vector<bool> vb;
typedef vector<vector<bool>> vvb;

class Solution {
public:
    bool dfs(int i, int x, int y, vvb &done, vvc &board, int m, int n, string &word) {
        if(word[i] != board[x][y]) return false;
        if(i==word.size()-1) return true;
        done[x][y] = true;
        int dirX[4] = {0, 0, 1, -1};
        int dirY[4] = {1, -1, 0, 0}; 
        for(int j=0; j<4; j++) {
            int nextX = x + dirX[j];
            int nextY = y + dirY[j];
            if(nextX >= 0 && nextX < m && nextY >= 0 && nextY < n && !done[nextX][nextY]) {
                if(dfs(i+1, nextX, nextY, done, board, m, n, word)) return true;
            }
        }
        done[x][y] = false;
        return false;
    }
    bool exist(vector<vector<char>>& board, string word) {
        int m = board.size(), n = board[0].size();
        vvb done = vvb(m, vb(n, false));
        for(int x=0; x<m; x++) {
            for(int y=0; y<n; y++) {
                if(dfs(0, x, y, done, board, m, n, word)) return true;
            }
        }
        return false;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; vvc board; string word; bool ans;
    
    solution = Solution();
    board = {{'A','B','C','E'},{'S','F','C','S'},{'A','D','E','E'}};
    word = "ABCCED";
    ans = solution.exist(board, word);
    assert(ans==true);

    solution = Solution();
    board = {{'A','B','C','E'},{'S','F','C','S'},{'A','D','E','E'}};
    word = "SEE";
    ans = solution.exist(board, word);
    assert(ans==true);

    solution = Solution();
    board = {{'A','B','C','E'},{'S','F','C','S'},{'A','D','E','E'}};
    word = "ABCB";
    ans = solution.exist(board, word);
    assert(ans==false);

    solution = Solution();
    board = {{'a','a'}};
    word = "aaa";
    ans = solution.exist(board, word);
    assert(ans==false);
}