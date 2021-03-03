#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

class Solution {
// Down-Top DP like Fibonacci, Time: O(n), Space: O(1)
public:
    int climbStairs(int n) {
        if(n==1) return 1;
        if(n==2) return 2;
        int prevAns = 1;
        int curAns = 2;
        for(int i=3; i<=n; i++) {
            int tmpAns = curAns;
            curAns = prevAns + curAns;
            prevAns = tmpAns;
        }
        return curAns;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; int n; int ans;

    solution = Solution();
    n = 2;
    ans = solution.climbStairs(n);
    assert(ans==2);

    solution = Solution();
    n = 3;
    ans = solution.climbStairs(n);
    assert(ans==3);
}