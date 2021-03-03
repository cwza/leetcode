#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

/*
https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/discuss/91059/Java-O(n)-solution-using-Trie

ex: 
nums = [14, 11, 7, 2], binary_form = [1110, 1011, 0111, 0010]
Trie:
                root
            .          .
          0              1
        .   .          .   .
       0     1        0     1
        .      .        .     .
         1      1        1     1
        .        .        .   .
       0          1        1 0
       2          7       11 14
*/

class Solution {
// Trie, Time: O(n), Space: O(1)
    class TrieNode {
    public:
        TrieNode* links[2] = {nullptr};
        TrieNode(){}
    };
public:
    TrieNode *root = new TrieNode();
    int findMaximumXOR(vector<int>& nums) {
        int ans = 0;
        for(int num : nums) {
            TrieNode *create = root;
            TrieNode *search = root;
            int tmp = 0;
            for(int i = 31; i >= 0; i--) {
                int b = num>>i & 1; // The ith bit of num(count from right)
                // Create
                if(!create->links[b]) create->links[b] = new TrieNode();
                create = create->links[b];
                // Search
                if(search->links[1-b]) {
                    search = search->links[1-b];
                    tmp += 1<<i;
                } else {
                    search = search->links[b];
                }
            }
            ans = max(ans, tmp);
        }
        return ans;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; vi nums; int ans;

    solution = Solution();
    nums = {3,10,5,25,2,8};
    ans = solution.findMaximumXOR(nums);
    assert(ans==28);

    solution = Solution();
    nums = {0};
    ans = solution.findMaximumXOR(nums);
    assert(ans==0);

    solution = Solution();
    nums = {2,4};
    ans = solution.findMaximumXOR(nums);
    assert(ans==6);

    solution = Solution();
    nums = {8,10,2};
    ans = solution.findMaximumXOR(nums);
    assert(ans==10);

    solution = Solution();
    nums = {14,70,53,83,49,91,36,80,92,51,66,70};
    ans = solution.findMaximumXOR(nums);
    assert(ans==127);
}