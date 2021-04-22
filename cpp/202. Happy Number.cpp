#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define ar array

class Solution {
public:
    bool isHappy(int n) {
        for(int i = 0; i < 1e6; ++i) {
            if(n==1) {
                return true;
            }
            int nn = 0;
            while(n) {
                nn += (n%10)*(n%10);
                n /= 10;
            }
            n = nn;
        }
        return false;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);
    // freopen("input.txt", "r", stdin); 
    // freopen("output.txt", "w", stdout);
    Solution solution;
    int n = 19;
    cout << solution.isHappy(n);
}