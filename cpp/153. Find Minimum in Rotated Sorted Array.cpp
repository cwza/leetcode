#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

/*
O(n) solution is trivial, but there exists an O(logn) solution which uses binary search.
 2  3  4  5  6  7
------------------
 7 (2) 3  4  5  6
 6  7 (2) 3  4  5
 5  6  7 (2) 3  4
 4  5  6  7 (2) 3
 3  4  5  6  7 (2)
------------------
We observed that:
1. The numbers before minimum (2) is always greater than or equal to nums[0]
2. The numbers after minimum (2) is always less than nums[0]

Obviously we can use binary search:
if arr[m] >= arr[0]: search right, l=m+1
else: search left, r=m

Use binary search template:
g(m) = True if arr[m] < arr[0] else False
That is find an minimal m such that arr[m] < arr[0]

Notice that if nums is not be rotated, we can't use above.
How to check if nums is rotated or not??
By observation, if nums[-1] > nums[0]: not rotated, else: rotated
*/

class Solution {
public:
    int findMin(vector<int>& nums) {
        int n = nums.size();
        if(nums.back() >= nums[0]) return nums[0];

        int l = 0, r = n;
        while(l < r) {
            int m = l + (r-l)/2;
            if(nums[m] < nums[0]) r = m;
            else l = m+1;
        }
        return nums[l];
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; vi nums; int ans;

    solution = Solution();
    nums = {3,4,5,1,2};
    ans = solution.findMin(nums);
    assert(ans==1);

    solution = Solution();
    nums = {4,5,6,7,0,1,2};
    ans = solution.findMin(nums);
    assert(ans==0);

    solution = Solution();
    nums = {11,13,15,17};
    ans = solution.findMin(nums);
    assert(ans==11);
}