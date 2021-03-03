#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

class Solution {
public:
    string longestWord(vector<string>& words) {
        unordered_set<string> table(words.begin(), words.end());       
        string ans = "";
        for(string word : words) {
            if(word.size() < ans.size()) continue;
            if(word.size() == ans.size() && word >= ans) continue;
            bool flag = true;
            for(int l=1; l<word.size(); l++) {
                if(!table.count(word.substr(0, l))) {
                    flag = false;
                    break;
                }
            }
            if(flag==true) ans = word;
        }
        return ans;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; vector<string> words; string ans;

    solution = Solution();
    words = {"w","wo","wor","worl", "world"};
    ans = solution.longestWord(words);
    assert(ans=="world");

    solution = Solution();
    words = {"a", "banana", "app", "appl", "ap", "apply", "apple"};
    ans = solution.longestWord(words);
    assert(ans=="apple");
}