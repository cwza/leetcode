#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

/*
Key:
if num is even then num >> 1 will not change the number of 1's, because the right most digit for even is always 0.
if num is odd then num >> 1 will decrease the number of 1's by 1, because the right most digit for odd is always 1.

Recurrence:
dp[i] = dp[i>>1] if i is even else dp[i>>1]+1
dp[0] = 0, dp[1] = 1
*/

class Solution {
// DP, Time: O(n), Space: O(n)
public:
    vector<int> countBits(int num) {
        if(num==0) return vi(1);
        vi dp(num+1, 0); dp[0] = 0, dp[1] = 1;
        for(int i = 2; i <= num; i++) {
            // if(i&1) dp[i] = dp[i>>1] + 1;
            // else dp[i] = dp[i>>1];
            dp[i] = dp[i>>1] + (i&1);
        }
        return dp;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; int num; vi ans;

    solution = Solution();
    num = 2;
    ans = solution.countBits(num);
    assert(ans==vi({0,1,1}));

    solution = Solution();
    num = 5;
    ans = solution.countBits(num);
    assert(ans==vi({0,1,1,2,1,2}));
}