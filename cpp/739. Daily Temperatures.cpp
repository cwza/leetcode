#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

class Solution {
// Monotonic decreasing deque, Time: O(n), Space: O(n)
public:
    vector<int> dailyTemperatures(vector<int>& T) {
        int n = T.size();
        deque<int> d; // We store idx in deque, the values are decreasing
        vi ans(n);
        for(int i = n-1; i >=0; i--) {
            while(d.size() && T[d.back()] <= T[i]) d.pop_back();
            if(d.size()) ans[i] = d.back() - i;
            else ans[i] = 0;
            d.push_back(i);
        }
        return ans;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; vi T, ans;

    T = {73, 74, 75, 71, 69, 72, 76, 73};
    ans = solution.dailyTemperatures(T);
    assert(ans==vi({1, 1, 4, 2, 1, 1, 0, 0}));
}