#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

class Solution {
// Binary Search + 2 Pointers
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        int n = arr.size();
        // Binary search to find the minimal that larger than or equal to target
        int l = 0, r = n;
        while(l < r) {
            int m = l + (r-l)/2;
            if(arr[m] >= x) r = m;
            else l = m + 1;
        }
        // Two pointer to find the result
        r = l, l = l-1;
        while(k--) {
            if(r >= n) l -= 1;
            else if(l < 0) r += 1;
            else if(abs(arr[l]-x) <= abs(arr[r]-x)) l -= 1;
            else r += 1;
        }
        return vi(arr.begin()+l+1, arr.begin()+r);
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; vi arr; int k, x; vi ans;

    solution = Solution();
    arr = {1,2,3,4,5};
    k = 4, x = 3;
    ans = solution.findClosestElements(arr, k, x);
    assert(ans==vi({1,2,3,4}));

    solution = Solution();
    arr = {1,2,3,4,5};
    k = 4, x = -1;
    ans = solution.findClosestElements(arr, k, x);
    assert(ans==vi({1,2,3,4}));
}