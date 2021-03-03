#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

// class Solution {
// // Search from right-top, Time: O(m+n)
// public:
//     bool searchMatrix(vector<vector<int>>& matrix, int target) {
//         int m = matrix.size(), n = matrix[0].size();
//         int i = 0, j = n-1;
//         while(i < m && j >= 0) {
//             if(matrix[i][j] == target) return true;
//             if(matrix[i][j] > target) j -= 1;
//             else i += 1;
//         }
//         return false;
//     }
// };

class Solution {
// Binary Search, O(logm + logn)
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m = matrix.size(), n = matrix[0].size();
        // Find rowIdx
        int l = 0, r = m;
        while(l < r) {
            int mid = l + (r-l)/2;
            if(matrix[mid][0] > target) r = mid;
            else l = mid + 1;
        }
        int rowIdx = l - 1;
        if(rowIdx == -1) return false;

        // Run regular binary search at rowIdx 
        l = 0, r = n;
        while(l < r) {
            int mid = l + (r-l)/2;
            if(matrix[rowIdx][mid] == target) return true;
            if(matrix[rowIdx][mid] > target) r = mid;
            else l = mid + 1;
        }
        return false;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; vvi matrix; int target; bool ans;

    solution = Solution();
    matrix = {{1,3,5,7},{10,11,16,20},{23,30,34,60}};
    target = 3;
    ans = solution.searchMatrix(matrix, target);
    assert(ans==true);

    solution = Solution();
    matrix = {{1,3,5,7},{10,11,16,20},{23,30,34,60}};
    target = 13;
    ans = solution.searchMatrix(matrix, target);
    assert(ans==false);
}