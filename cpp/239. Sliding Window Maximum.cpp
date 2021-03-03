#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

// class Solution {
// // Monotonic Decreasing Deque, Time: O(n), Space: O(k)
// public:
//     vector<int> maxSlidingWindow(vector<int>& nums, int k) {
//         deque<int> d; // We store idx in deque, the values are decreasing
//         int n = nums.size();
//         vi ans;
//         for(int i = 0; i < n; i++) {
//             while(d.size() && nums[d.back()] <= nums[i]) d.pop_back(); // Maintain the decreasing order
//             while(d.size() && d.front() <= i-k) d.pop_front(); // Maintain the window size
//             d.push_back(i);
//             if(i >= k-1) ans.push_back(nums[d.front()]);
//         }
//         return ans;
//     }
// };

class Solution {
// Balanced Binary Search Tree, Time: O(nlogk), Space: O(k)
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        int n = nums.size();
        multiset<int> bt(nums.begin(), nums.begin()+k);
        vi ans;
        ans.push_back(*bt.rbegin());
        for(int i = k; i < n; i++) {
            bt.erase(bt.find(nums[i-k])); // O(logk)
            bt.insert(nums[i]); // O(logk)
            ans.push_back(*bt.rbegin()); // O(1)
        }
        return ans;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; vi nums; int k; vi ans;

    nums = {1,3,-1,-3,5,3,6,7}, k = 3;
    ans = solution.maxSlidingWindow(nums, k);
    assert(ans == vi({3,3,5,5,6,7}));

    nums = {1}, k = 1;
    ans = solution.maxSlidingWindow(nums, k);
    assert(ans == vi({1}));

    nums = {1,-1}, k = 1;
    ans = solution.maxSlidingWindow(nums, k);
    assert(ans == vi({1,-1}));

    nums = {9,11}, k = 2;
    ans = solution.maxSlidingWindow(nums, k);
    assert(ans == vi({11}));

    nums = {4,-2}, k = 2;
    ans = solution.maxSlidingWindow(nums, k);
    assert(ans == vi({4}));
}