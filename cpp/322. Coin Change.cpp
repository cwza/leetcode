#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

/*
dp[x] = min(dp[x-coin for coin in coins) + 1
dp[0] = 0
*/

class Solution {
// Time: O(amount*n), Space: O(amount)
public:
    int coinChange(vector<int>& coins, int amount) {
        int dp[amount+1]; fill(dp, dp+amount+1, INT_MAX); dp[0] = 0;
        for(int x = 1; x <= amount; x++) {
            for(int coin : coins) {
                if(x-coin < 0) continue;
                dp[x] = min(dp[x], dp[x-coin]);
            }
            if(dp[x] != INT_MAX) dp[x] += 1;
        }
        return dp[amount] == INT_MAX ? -1 : dp[amount];
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; vi coins; int amount; int ans;

    solution = Solution();
    coins = {1,2,5};
    amount = 11;
    ans = solution.coinChange(coins, amount);
    assert(ans==3);

    solution = Solution();
    coins = {2};
    amount = 3;
    ans = solution.coinChange(coins, amount);
    assert(ans==-1);

    solution = Solution();
    coins = {1};
    amount = 0;
    ans = solution.coinChange(coins, amount);
    assert(ans==0);

    solution = Solution();
    coins = {1};
    amount = 1;
    ans = solution.coinChange(coins, amount);
    assert(ans==1);

    solution = Solution();
    coins = {1};
    amount = 2;
    ans = solution.coinChange(coins, amount);
    assert(ans==2);
}