#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define ar array

class Solution {
public:
    static const int maxN = 20;
    string S[maxN+1];
    Solution() {
        S[1] = "0";
    }
    void pre(int n) {
        for(int i = 2; i <= n; ++i) {
            string s2(S[i-1].size(), ' ');
            for(int j = 0; j < S[i-1].size(); ++j) {
                s2[S[i-1].size()-j-1] = S[i-1][j]=='0'?'1':'0';
            }
            S[i] = S[i-1] + '1' + s2;
        }
    }
    char findKthBit(int n, int k) {
        pre(n);
        return S[n][k-1];
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);
    // freopen("input.txt", "r", stdin); 
    // freopen("output.txt", "w", stdout);
    int n, k;
    Solution solution;
    n = 3, k = 1;
    cout << solution.findKthBit(n, k) << endl;
    n = 4, k = 11;
    cout << solution.findKthBit(n, k) << endl;
    n = 1, k = 1;
    cout << solution.findKthBit(n, k) << endl;
    n = 2, k = 3;
    cout << solution.findKthBit(n, k) << endl;
}