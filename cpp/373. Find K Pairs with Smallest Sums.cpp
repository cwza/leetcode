#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;
typedef tuple<int, int, int> ti;

/*
Almostly same as Leetcode 378
nums1 = [1, 7, 11], nums2 = [2, 4, 6]
     2  4  6
   ----------
1 |  3  5  7 
7 |  9 11 13
11| 13 15 17
*/

class Solution {
// MinHeap, Time: O(klogk), Space: O(k)
public:
    vector<vector<int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k) {
        int m = nums1.size(), n = nums2.size();
        if(m == 0 || n == 0 || k == 0) return vvi();
        auto comp = [](ti &lhs, ti &rhs) {
            return lhs > rhs;
        };
        priority_queue<ti, vector<ti>, decltype(comp)> pq(comp);
        for(int j = 0; j < min(n, k); j++) {
            auto element = make_tuple(nums1[0]+nums2[j], 0, j);
            pq.push(element);
        }      
        vvi ans; 
        while(pq.size() && k--) {
            auto [val, x, y] = pq.top(); pq.pop();
            ans.push_back(vi({nums1[x], nums2[y]}));
            if(x+1 < m) pq.push(make_tuple(nums1[x+1]+nums2[y], x+1, y));
        }
        return ans;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; vi nums1, nums2; int k; vvi ans;

    solution = Solution();
    nums1 = {1,7,11}, nums2 = {2,4,6}, k = 3;
    ans = solution.kSmallestPairs(nums1, nums2, k);
    assert(ans==vvi({{1,2},{1,4},{1,6}}));

    solution = Solution();
    nums1 = {1,1,2}, nums2 = {1,2,3}, k = 2;
    ans = solution.kSmallestPairs(nums1, nums2, k);
    assert(ans==vvi({{1,1},{1,1}}));
}