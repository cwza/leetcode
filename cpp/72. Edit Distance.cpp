#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

/*
https://www.youtube.com/watch?v=ocZMDMZwhCY&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=21

dp[i][j]: edit_distance(word1[0,i+1], word2[0,j+1])
dp[0][0] = 0
dp[0][i] = i
dp[i][0] = j
dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1 if word1[i] != word2[j]
dp[i][j] = dp[i-1][j-1] if word1[i] == word2[j]

ex: 
    r o s
  0 1 2 3 
h|1 1 2 3 
o|2 2 1 2 
r|3 2 2 2 
s|4 3 3 2 
e|5 4 4 3 
*/

class Solution {
// DP, Time: O(nm), Space: O(nm), n: len(word1), m: len(word2)
public:
    int minDistance(string word1, string word2) {
        int m = word1.size()+1, n = word2.size()+1;
        int dp[m][n]; fill(&dp[0][0], &dp[0][0]+m*n, 0);

        for(int i=0; i<m; i++) {
            for(int j=0; j<n; j++) {
                if(i==0 && j==0) {
                    dp[i][j] = 0;
                } else if(i==0) {
                    dp[i][j] = j;
                } else if(j==0) {
                    dp[i][j] = i;
                } else {
                    if(word1[i-1]==word2[j-1]) dp[i][j] = dp[i-1][j-1];
                    else dp[i][j] = min({dp[i-1][j], dp[i][j-1], dp[i-1][j-1]}) + 1;
                }
                // cout << dp[i][j] << " ";
            }
            // cout << "\n";
        }
        return dp[m-1][n-1];
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; string word1; string word2; int ans;

    solution = Solution();
    word1 = "horse", word2 = "ros";
    ans = solution.minDistance(word1, word2);
    assert(ans==3);

    solution = Solution();
    word1 = "intention", word2 = "execution";
    ans = solution.minDistance(word1, word2);
    assert(ans==5);
}