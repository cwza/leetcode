#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define ar array

class Solution {
public:
    bool check(char a, char b) {
        if(a!=b && tolower(a)==tolower(b)) {
            return false;
        }
        return true;
    }
    string makeGood(string s) {
        bool change = true;
        while(change) {
            change = false;
            for(int i = 0; i < (int)s.size()-1; ++i) {
                if(s[i]+32==s[i+1] || s[i+1]+32==s[i]) {
                    s.erase(i, 2);
                    change = true;
                    break;
                }
            }
        }
        return s;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);
    // freopen("input.txt", "r", stdin); 
    // freopen("output.txt", "w", stdout);
    string s = "";
    Solution solution = Solution();
    s = "leEeetcode";
    cout << solution.makeGood(s) << endl;
    s = "abBAcC";
    cout << solution.makeGood(s) << endl;
    s = "s";
    cout << solution.makeGood(s) << endl;
}