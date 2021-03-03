#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

/*
Compare to Leetcode 377, just exchange the two loop order.
The 377 ask for permutation but this one ask for combination.
*/

class Solution {
public:
    int change(int amount, vector<int>& coins) {
        unsigned int dp[amount+1]; fill(dp, dp+amount+1, 0); dp[0] = 1;
        for(int num : coins) {
            for(int i=1; i<=amount; i++) {
                if(i-num >=0) {
                    dp[i] += dp[i-num];
                }
            }
        }
        return dp[amount];
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; int amount; vi coins; int ans;

    solution = Solution();
    amount = 5, coins = {1, 2, 5};
    ans = solution.change(amount, coins);
    assert(ans==4);

    solution = Solution();
    amount = 3, coins = {2};
    ans = solution.change(amount, coins);
    assert(ans==0);

    solution = Solution();
    amount = 10, coins = {10};
    ans = solution.change(amount, coins);
    assert(ans==1);
}