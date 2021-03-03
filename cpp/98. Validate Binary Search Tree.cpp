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
// Inorder of BST is definitely sorted
public:
    bool dfs(TreeNode *root, int &pre, bool &isFirst) {
        if(!root) return true;
        if(!dfs(root->left, pre, isFirst)) return false;
        if(!isFirst && root->val <= pre) return false;
        pre = root->val;
        isFirst = false;
        if(!dfs(root->right, pre, isFirst)) return false;
        return true;
    }
    bool isValidBST(TreeNode* root) {
        int pre = INT_MIN;
        bool isFirst = true;
        return dfs(root, pre, isFirst);
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    
}