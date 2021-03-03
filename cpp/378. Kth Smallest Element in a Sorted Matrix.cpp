#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;
typedef tuple<int, int, int> ti;

class Solution {
// MinHeap, Time: O(klogk), Space: O(k)
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        int m = matrix.size(), n = matrix[0].size();
        auto comp = [](ti &lhs, ti &rhs) {
            return get<0>(lhs) > get<0>(rhs);
        };
        priority_queue<ti, vector<ti>, decltype(comp)> pq(comp); // MinQueue of value (value, x, y)
        for(int j = 0; j < min(n, k); j++) { // Put 1st row into priority queue
            auto element = make_tuple(matrix[0][j], 0, j);
            pq.push(element);
        }
        int ans;
        for(int i = 0; i < k; i++) {
            auto [val, x, y] = pq.top(); pq.pop();
            ans = val;
            if(x+1 < m) pq.push(make_tuple(matrix[x+1][y], x+1, y));
        }
        return ans;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; vvi matrix; int k, ans;

    solution = Solution();
    matrix = {
        { 1,  5,  9},
        {10, 11, 13},
        {12, 13, 15}
    };
    k = 8;
    ans = solution.kthSmallest(matrix, k);
    assert(ans==13);
}