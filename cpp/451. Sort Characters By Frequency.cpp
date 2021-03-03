#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

// class Solution {
// // Custom sort on frequency, Time: O(n+26log26), Space: O(26), Suppose size of characters is constant.
// public:
//     string frequencySort(string s) {
//         unordered_map<char, int> counter;
//         for(char ch : s) counter[ch]++;
//         vector<pair<char, int>> data(counter.begin(), counter.end()); // [(ch, freq)]
//         auto comp = [](pair<char, int> &lhs, pair<char, int> &rhs) {
//             return lhs.second > rhs.second;
//         };
//         sort(data.begin(), data.end(), comp);

//         string ans = "";
//         for(auto [ch, freq] : data) {
//             for(int i = 0; i < freq; i++) ans.push_back(ch);
//         }
//         return ans;
//     }
// };

class Solution {
// Bucket Sort because freq will never greater than n, Time: O(n), Space: O(n)
public:
    string frequencySort(string s) {
        int n = s.size();
        unordered_map<char, int> counter;
        for(char ch : s) counter[ch]++;
        vector<vector<char>> bucket(n+1, vector<char>());
        for(auto [ch, freq] : counter) bucket[freq].push_back(ch);
        string ans = "";
        for(int freq = n; freq >= 0; freq--) {
            for(char ch : bucket[freq]) for(int j = 0; j < freq; j++) ans.push_back(ch);
        }
        return ans;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; string s, ans;

    s = "tree";
    ans = solution.frequencySort(s);
    assert(ans=="eert");

    s = "cccaaa";
    ans = solution.frequencySort(s);
    assert(ans=="cccaaa" || ans=="aaaccc");

    s = "Aabb";
    ans = solution.frequencySort(s);
    assert(ans=="bbAa" || ans=="bbaA");
}