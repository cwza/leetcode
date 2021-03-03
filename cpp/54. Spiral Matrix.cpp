#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef vector<bool> vb;
typedef vector<vector<bool>> vvb;
typedef pair<int, int> pi;

class Board {
public:
    int m, n;
    // dir: {0: right, 1: down, 2: left, 3: up}
    pair<int, int> dirToMove[4] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    int curI = 0, curJ = -1, curDir = 0;
    vvb done; int doneCount = 0;
    Board(int m, int n):m(m), n(n), done(vvb(m, vb(n, false))){}
    void nextDir() {
        curDir = (curDir + 1) % 4;
    }
    bool go() {
        if(doneCount==m*n) return false;
        int nextI = curI + dirToMove[curDir].first;
        int nextJ = curJ + dirToMove[curDir].second;
        if(nextI < 0 || nextI >= m || nextJ < 0 || nextJ >= n || done[nextI][nextJ]) {
            nextDir();
            return go();
        } 
        curI = nextI;
        curJ = nextJ;
        done[nextI][nextJ] = true;
        doneCount++;
        return true;
    }
};

class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        Board board(matrix.size(), matrix[0].size());
        vi ans;
        while(board.go()) {
            ans.push_back(matrix[board.curI][board.curJ]);
        }
        return ans;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; vvi matrix; vi ans;

    solution = Solution();
    matrix = {{1,2,3},{4,5,6},{7,8,9}};
    ans = solution.spiralOrder(matrix);
    assert(ans==vi({1,2,3,6,9,8,7,4,5}));

    solution = Solution();
    matrix = {{1,2,3,4},{5,6,7,8},{9,10,11,12}};
    ans = solution.spiralOrder(matrix);
    assert(ans==vi({1,2,3,4,8,12,11,10,9,5,6,7}));
}