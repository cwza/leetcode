#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

/*
https://www.youtube.com/watch?v=oL6mRyTn56M

rest: rest(cooldown), sold(cooldown)
hold: rest(buy), hold(cooldown)
sold: hold(sell)

rest[i] = max(rest[i-1], sold[i-1]) # max profit if rest or cooldown on ith day
hold[i] = max(hold[i-1], rest[i-1]-prices[i]) # max profit if hold stock on ith day
sold[i] = hold[i-1]+prices[i] # max profit if sold stock on ith day

rest[0] = 0
hold[0] = -prices[0]
sold[0] = -inf

ans = max(rest[n-1], sold[n-1])
*/

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        if(n == 0) return 0;
        int rest[n]; rest[0] = 0; 
        int hold[n]; hold[0] = -prices[0];
        int sold[n]; sold[0] = INT_MIN;
        for(int i = 1; i < n; i++) {
            rest[i] = max(rest[i-1], sold[i-1]);
            hold[i] = max(hold[i-1], rest[i-1]-prices[i]);
            sold[i] = hold[i-1] + prices[i];
        }
        return max(rest[n-1], sold[n-1]);
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; vi prices; int ans;

    solution = Solution();
    prices = {1,2,3,0,2};
    ans = solution.maxProfit(prices);
    assert(ans==3);
}