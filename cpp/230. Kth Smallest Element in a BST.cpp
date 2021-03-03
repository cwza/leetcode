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
// Recursive inorder traversal, Time: O(n), Space: O(n)
public:
    void dfs(TreeNode *root, vi &arr) {
        if(!root) return;
        dfs(root->left, arr);
        arr.push_back(root->val);
        dfs(root->right, arr);
    }
    int kthSmallest(TreeNode* root, int k) {
        vi arr;
        dfs(root, arr);
        return arr[k-1];
    }
};

class Solution {
// Iterative inorder traversal, Time: O(k), Space: O(n)
public:
    void helper(TreeNode *node, stack<TreeNode*> &s) {
        while(node) {
            s.push(node);
            node = node->left;
        }
    }
    int kthSmallest(TreeNode* root, int k) {
        stack<TreeNode*> s;
        helper(root, s);

        int ans = 0;
        while(k--) {
            TreeNode *node = s.top(); s.pop();
            ans = node->val;
            if(node->right) helper(node->right, s);
        }
        return ans;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

}