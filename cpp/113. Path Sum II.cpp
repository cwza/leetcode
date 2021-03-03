#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;


struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    void dfs(TreeNode *root, int target, vi &path, vvi &ans) {
        if(!root->left && !root->right && target==root->val) {
            path.push_back(root->val);
            ans.push_back(path);
            path.pop_back();
            return;
        }
        if(root->left) {
            path.push_back(root->val);
            dfs(root->left, target-root->val, path, ans);
            path.pop_back();
        }
        if(root->right) {
            path.push_back(root->val);
            dfs(root->right, target-root->val, path, ans);
            path.pop_back();
        }
    }
    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        if(!root) return vvi();
        vi path;
        vvi ans;
        dfs(root, sum, path, ans);
        return ans;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    
}