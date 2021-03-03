#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

class Solution {
// Time: O(n), Space: O(1)
public:
    int maxProfit(vector<int>& prices) {
        if(prices.size()==0) return 0;

        int curMin = prices[0];
        int ans = 0;
        for(int i=1; i<prices.size(); i++) {
            ans = max(ans, prices[i]-curMin);
            curMin = min(curMin, prices[i]);
        }     
        return ans;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    
}