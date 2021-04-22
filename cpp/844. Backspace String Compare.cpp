#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define ar array

class Solution {
public:
    bool backspaceCompare(string s, string t) {
        string ss = "", tt = "";
        for(char ch : s) {
            if(ch != '#') {
                ss.push_back(ch);
            } else {
                if(ss.size()!=0) {
                    ss.pop_back();
                }
            }
        }
        for(char ch : t) {
            if(ch != '#') {
                tt.push_back(ch);
            } else {
                if(tt.size()!=0) {
                    tt.pop_back();
                }
            }
        }
        return ss == tt;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);
    // freopen("input.txt", "r", stdin); 
    // freopen("output.txt", "w", stdout);

    string s, t;
    Solution solution;
    s = "ab##", t = "c#d#";
    cout << solution.backspaceCompare(s, t) << "\n";
}