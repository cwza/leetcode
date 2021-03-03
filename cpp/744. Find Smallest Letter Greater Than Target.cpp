#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

class Solution {
// Time: O(logn), Space: O(1)
public:
    char nextGreatestLetter(vector<char>& letters, char target) {
        int l = 0, r = letters.size();
        while(l < r) {
            int m = l + (r-l)/2;
            if(letters[m] > target) r = m;
            else l = m + 1;
        }
        if(l == letters.size()) return letters[0];
        return letters[l];
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; vector<char> letters; char target; char ans;
    
    solution = Solution();
    letters = {'c', 'f', 'j'}, target = 'a';
    ans = solution.nextGreatestLetter(letters, target);
    assert(ans=='c');
}