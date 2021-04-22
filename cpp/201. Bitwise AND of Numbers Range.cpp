#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define ar array

// https://www.youtube.com/watch?v=6aHmj9ihjMY
class Solution {
public:
    int rangeBitwiseAnd(int left, int right) {
        int ans = 0;
        for(int i = 30; i >= 0; --i) {
            if( (left&(1<<i)) == (right&(1<<i)) ) {
                ans |= left&(1<<i);
            } else {
                break;
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
}