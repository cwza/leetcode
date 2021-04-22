#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define ar array

/*
Just add up the positive adjacent diffs
*/

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int ans = 0;
        for(int i = 0; i < prices.size()-1; ++i) {
            if(prices[i+1] > prices[i]) {
                ans += prices[i+1]-prices[i];
            }
        }
        return ans;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);
    // freopen("input.txt", "r", stdin); 
    // freopen("output.txt", "w", stdout);
    vector<int> prices;
    Solution solution;
    prices = {7,1,5,3,6,4};
    cout << solution.maxProfit(prices); // 7
}