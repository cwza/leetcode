#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int m = matrix.size(), n = matrix[0].size();
        for(int i = 0; i < m; i++) {
            for(int j = i + 1; j < n; j++) {
                swap(matrix[i][j], matrix[j][i]);
            }
        }
        for(auto &row : matrix) {
            reverse(row.begin(), row.end());
        }
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; vvi matrix;

    solution = Solution();
    matrix = {{1,2,3},{4,5,6},{7,8,9}};
    solution.rotate(matrix);
    assert(matrix==vvi({{7,4,1},{8,5,2},{9,6,3}}));

    solution = Solution();
    matrix = {{5,1,9,11},{2,4,8,10},{13,3,6,7},{15,14,12,16}};
    solution.rotate(matrix);
    assert(matrix==vvi({{15,13,2,5},{14,3,4,1},{12,6,8,9},{16,7,10,11}}));
}