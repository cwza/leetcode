#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

/*
One pass is tricky please see:

The intuition behind this approach is that the area formed between the lines will always be limited by the height of the shorter line. Further, the farther the lines, the more will be the area obtained.
We take two pointers, one at the beginning and one at the end of the array constituting the length of the lines. 
Futher, we maintain a variable maxarea to store the maximum area obtained till now. 
At every step, we find out the area formed between them, update maxarea and move the pointer pointing to the shorter line towards the other end by one step.
https://www.youtube.com/watch?v=cPwXGcZQ1mA&ab_channel=JoyLiu-ComputerPsyc
*/

class Solution {
// Two Pointers, Time: O(n), Space: O(1)
public:
    int maxArea(vector<int>& height) {
        int n = height.size();
        int ans = 0;       
        int l = 0, r = n-1;
        while(l < r) {
            int area = min(height[l], height[r]) * (r-l);
            ans = max(ans, area);
            if(height[l] <= height[r]) l++;
            else r--;
        }
        return ans;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; vi height; int ans;

    height = {1,8,6,2,5,4,8,3,7};
    ans = solution.maxArea(height);
    assert(ans==49);
}