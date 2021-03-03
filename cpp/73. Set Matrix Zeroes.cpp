#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

class Solution {
// Time: O(mn), Space: O(1)
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int m = matrix.size(), n = matrix[0].size();
        bool isRow = false, isCol = false;
        for(int i=0; i<m; i++) {
            if(matrix[i][0]==0) {
                isCol = true;
                break;
            }
        }
        for(int j=0; j<n; j++) {
            if(matrix[0][j]==0) {
                isRow = true;
                break;
            }
        }
        for(int i=0; i<m; i++) {
            for(int j=0; j<n; j++) {
                if(matrix[i][j] == 0) {
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }
        }
        for(int i=1; i<m; i++) {
            for(int j=1; j<n; j++) {
                if(matrix[i][0]==0 or matrix[0][j]==0) matrix[i][j] = 0;
            }
        }
        if(isRow) {
            fill(&matrix[0][0], &matrix[0][0]+n, 0);
        }
        if(isCol) {
            for(int i=1; i<m; i++) {
                matrix[i][0] = 0;
            }
        }
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; vvi matrix;

    solution = Solution();
    matrix = {{1,1,1},{1,0,1},{1,1,1}};
    solution.setZeroes(matrix);
    assert(matrix==vvi({{1,0,1},{0,0,0},{1,0,1}}));

    solution = Solution();
    matrix = {{0,1,2,0},{3,4,5,2},{1,3,1,5}};
    solution.setZeroes(matrix);
    assert(matrix==vvi({{0,0,0,0},{0,4,5,0},{0,3,1,0}}));
}