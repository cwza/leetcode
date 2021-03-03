#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

class Solution {
// Sliding Window, Time: O(n), Space: O(1)
public:
    int totalFruit(vector<int>& tree) {
        int n = tree.size();       
        int l = 0;
        unordered_map<int, int> counter;
        int ans = 0;
        for(int r = 0; r < n; r++) {
            counter[tree[r]] += 1;
            while(counter.size() > 2) {
                counter[tree[l]] -= 1;
                if(counter[tree[l]] == 0) counter.erase(tree[l]);
                l += 1;
            }
            ans = max(ans, r-l+1);
        }
        return ans;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; vi tree; int ans;

    tree = {1,2,1};
    ans = solution.totalFruit(tree);
    assert(ans==3);
    
    tree = {0,1,2,2};
    ans = solution.totalFruit(tree);
    assert(ans==3);

    tree = {1,2,3,2,2};
    ans = solution.totalFruit(tree);
    assert(ans==4);

    tree = {3,3,3,1,2,1,1,2,3,3,4};
    ans = solution.totalFruit(tree);
    assert(ans==5);
}