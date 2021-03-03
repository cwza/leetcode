#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

/*
How to check whether one string is a permutation of another string?
1. Sort the string and then compare
2. Both strings must have same character frequencies
*/

class Solution {
// Sliding Window + HashMap
public:
    bool checkInclusion(string s1, string s2) {
        int windowSize = s1.size(), n = s2.size();
        if(windowSize > n) return false;

        unordered_map<char, int> s1Counter, s2Counter;
        for(int i = 0; i < windowSize; i++) {
            s1Counter[s1[i]] += 1;
            s2Counter[s2[i]] += 1;
        }
        if(s1Counter==s2Counter) return true;

        for(int l = 1; l <= n-windowSize; l++) {
            int r = l + windowSize - 1;
            s2Counter[s2[l-1]] -= 1;
            if(s2Counter[s2[l-1]] == 0) s2Counter.erase(s2[l-1]); 
            s2Counter[s2[r]] += 1;
            if(s1Counter==s2Counter) return true;
        }
        return false;
    }
};

class Solution {
// Sliding Window + Array
public:
    bool checkInclusion(string s1, string s2) {
        int windowSize = s1.size(), n = s2.size();
        if(windowSize > n) return false;

        int s1Counter[26] = {0}, s2Counter[26] = {0};
        for(int i = 0; i < windowSize; i++) {
            s1Counter[s1[i]-'a'] += 1;
            s2Counter[s2[i]-'a'] += 1;
        }
        if(equal(s1Counter, s1Counter+26, s2Counter)) return true;

        for(int l = 1; l <= n-windowSize; l++) {
            int r = l + windowSize - 1;
            s2Counter[s2[l-1]-'a'] -= 1;
            s2Counter[s2[r]-'a'] += 1;
            if(equal(s1Counter, s1Counter+26, s2Counter)) return true;
        }
        return false;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; string s1, s2; bool ans;

    s1 = "ab", s2 = "eidbaooo";
    ans = solution.checkInclusion(s1, s2);
    assert(ans==true);

    s1 = "ab", s2 = "eidboaoo";
    ans = solution.checkInclusion(s1, s2);
    assert(ans==false);
}