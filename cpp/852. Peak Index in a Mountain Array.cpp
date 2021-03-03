#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

class Solution {
// Binary Search, Time: O(logn), Space: O(1)
public:
    int peakIndexInMountainArray(vector<int>& arr) {
        int l = 0, r = arr.size();
        while(l < r) {
            int m = l + (r-l)/2;
            if (arr[m+1] < arr[m]) r = m;
            else l = m + 1;
        }
        return l;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution = Solution();
    vi arr = {24,69,100,99,79,78,67,36,26,19};
    int ans = solution.peakIndexInMountainArray(arr);
    assert(ans==2);
}