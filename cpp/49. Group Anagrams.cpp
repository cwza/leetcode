#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define ar array

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<ar<int, 26>, vector<string>> ma;
        for(string str : strs) {
            ar<int, 26> cnt = {};
            for(char ch : str) {
                cnt[ch-'a']++;
            }
            ma[cnt].push_back(str);
        }
        vector<vector<string>> ans;
        for(auto a : ma) {
            ans.push_back(a.second);
        }
        return ans;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);
    // freopen("input.txt", "r", stdin); 
    // freopen("output.txt", "w", stdout);

    vector<string> strs;
    Solution solution;
    strs = {"eat","tea","tan","ate","nat","bat"};
    solution.groupAnagrams(strs);
}