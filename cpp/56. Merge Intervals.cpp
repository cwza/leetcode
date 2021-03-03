#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end());
        vvi ans;       
        ans.push_back(intervals[0]);
        for(int i = 1; i < intervals.size(); i++) {
            vi a = ans.back();
            vi b = intervals[i];
            if(b[0] > a[1]) ans.push_back(b);
            else ans.back() = vi({a[0], max(a[1], b[1])});
        }
        return ans;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; vvi intervals, ans;

    solution = Solution();
    intervals = {{1,3},{2,6},{8,10},{15,18}};
    ans = solution.merge(intervals);
    assert(ans==vvi({{1,6},{8,10},{15,18}}));

    solution = Solution();
    intervals = {{1,4},{4,5}};
    ans = solution.merge(intervals);
    assert(ans==vvi({{1,5}}));
}