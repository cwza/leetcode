#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

class Solution {
public:
    vector<vector<string>> solveNQueens(int n) {
        // backtracking, Time: O(n!)
        vector<bool> colStatus(n, true);
        vector<bool> diag1Status(2*n-1, true);
        vector<bool> diag2Status(2*n-1, true);

        vector<string> board(n, string(n, '.'));
        vector<vector<string>> ans;
        function<void(int)> dfs = [&](int row) {
            if(row==n) {
                ans.push_back(board);
                return;
            }
            for(int col=0; col<n; col++) {
                if(colStatus[col] && diag1Status[row+col] && diag2Status[row-col+(n-1)]) {
                    colStatus[col] = false; diag1Status[row+col] = false; diag2Status[row-col+n-1] = false;
                    board[row][col] = 'Q';
                    dfs(row+1);
                    colStatus[col] = true; diag1Status[row+col] = true; diag2Status[row-col+n-1] = true;
                    board[row][col] = '.';
                }
            }
        };
        dfs(0);
        return ans;
    }
};

void printAns(vector<vector<string>> ans) {
    for(auto board: ans) {
        cout << "(";
        for(auto row: board) {
            cout << "\"" << row << "\"";
        }
        cout << ")";
    }
    cout << "\n";
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; int n; vector<vector<string>> ans, expected;

    solution = Solution();
    n = 4;
    ans = solution.solveNQueens(n);
    expected = {{".Q..","...Q","Q...","..Q."},{"..Q.","Q...","...Q",".Q.."}};
    printAns(ans);
    assert(ans==expected);

    solution = Solution();
    n = 1;
    ans = solution.solveNQueens(n);
    expected = {{"Q"}};
    printAns(ans);
    assert(ans==expected);
}