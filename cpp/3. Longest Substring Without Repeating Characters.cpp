#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

class Solution {
// Sliding Window, Time: O(n), Space: O(n)
public:
    int lengthOfLongestSubstring(string s) {
        int n = s.size();
        int l = 0, ans = 0;
        unordered_set<char> dupCheck;
        for(int r = 0; r < n; r++) {
            while(dupCheck.count(s[r])) {
                dupCheck.erase(s[l]);
                l += 1;
            }
            dupCheck.insert(s[r]);
            ans = max(ans, r-l+1);
        }
        return ans;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; string s; int ans;

    s = "abcabcbb";
    ans = solution.lengthOfLongestSubstring(s);
    assert(ans==3);

    s = "bbbbb";
    ans = solution.lengthOfLongestSubstring(s);
    assert(ans==1);

    s = "pwwkew";
    ans = solution.lengthOfLongestSubstring(s);
    assert(ans==3);

    s = "";
    ans = solution.lengthOfLongestSubstring(s);
    assert(ans==0);
}