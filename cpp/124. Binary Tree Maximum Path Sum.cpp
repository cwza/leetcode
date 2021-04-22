#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define ar array


struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
    int ans = -1e9;
public:
    int dfs(TreeNode* root) {
        int tmp = root->val;
        int l = 0, r = 0;
        if(root->left) {
            l = dfs(root->left);
        }
        if(root->right) {
            r = dfs(root->right);
        }
        ans = max({ans, tmp+l+r});
        return max(0, tmp + max(l, r));
    }
    int maxPathSum(TreeNode* root) {
        dfs(root);
        return ans;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);
    // freopen("input.txt", "r", stdin); 
    // freopen("output.txt", "w", stdout);
}