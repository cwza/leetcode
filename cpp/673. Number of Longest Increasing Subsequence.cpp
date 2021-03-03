#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

/*
length[i]: The LIS length from 0 to i, including i 
count[i]: The number of LIS from 0 to i, including i

Leetcode300 to get length[i]

Transition function:
count[i] =
1. for j = 0 ~ i-1:
       Find those j that satisfies nums[i] > nums[j] and make length[j] max
2. for such j in 1:
       count[i] += length[j]
Initial:
count[i] = 1

result:
1. For i = 0 ~ n-1:
       Find those i that make length[i] max
2. for such i in 1:
       result += count[i]
*/

class Solution {
// DP, Time: O(n^2), Space: O(n)
public:
    int findNumberOfLIS(vector<int>& nums) {
        int n = nums.size();
        int length[n];
        int count[n];
        int maxLen = 0;
        int ans = 0;
        for(int i = 0; i < n; i++) {
            length[i] = 1; count[i] = 1;
            for(int j = 0; j < i; j++) {
                if(nums[i] > nums[j]) {
                    if(length[j]+1 > length[i]) { // Because new length > old length, so we need to update
                        length[i] = length[j] + 1;
                        count[i] = count[j];
                    } else if(length[j]+1 == length[i]) { // This means we have the same length previously
                        count[i] += count[j];
                    }
                }
            }
            if(length[i] > maxLen) { // Update maxLen
                maxLen = length[i];
                ans = count[i];
            } else if(length[i] == maxLen) { // find same length
                ans += count[i];
            }
        }
        return ans;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; vi nums; int ans;

    solution = Solution();
    nums = {1,3,5,4,7};
    ans = solution.findNumberOfLIS(nums);
    assert(ans==2);
    
    solution = Solution();
    nums = {2,2,2,2,2};
    ans = solution.findNumberOfLIS(nums);
    assert(ans==5);
}