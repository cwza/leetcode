#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

class NumArray {
public:
    vi nums;
    vi prefixSum;
    NumArray(vector<int>& nums) : nums(nums), prefixSum(nums) {
        // Time: O(n), Space: O(n)
        int n = prefixSum.size();
        for(int i=1; i<n; i++) {
            prefixSum[i] = prefixSum[i-1] + nums[i];
        }
    }
    int sumRange(int i, int j) {
        // Time: O(1)
        if(i==0) return prefixSum[j];
        return prefixSum[j] - prefixSum[i-1];
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    NumArray *obj; vi nums; int ans;

    nums = {-2, 0, 3, -5, 2, -1};
    obj = new NumArray(nums);
    ans = obj->sumRange(0,2);
    assert(ans==1);
    ans = obj->sumRange(2,5);
    assert(ans==-1);
    ans = obj->sumRange(0,5);
    assert(ans==-3);
    delete obj;
}