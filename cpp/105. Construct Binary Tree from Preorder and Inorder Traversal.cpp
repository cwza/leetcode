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
    int prei = 0;
    vector<int> pre, in;
    map<int, int> numToIdx;
    TreeNode* helper(int ini, int inj) {
        int rootval = pre[prei];
        prei++;
        TreeNode *root = new TreeNode(rootval);
        int k = numToIdx[rootval];
        if(ini <= k-1) root->left = helper(ini, k-1);
        if(k+1 <= inj) root->right = helper(k+1, inj);
        return root;
    }
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        pre = preorder, in = inorder;
        for(int i = 0; i < in.size(); i++) numToIdx[in[i]] = i;
        return helper(0, in.size()-1);
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; vi preorder, inorder; TreeNode *ans;

    preorder = {3,9,20,15,7};
    inorder = {9,3,15,20,7};
    ans = solution.buildTree(preorder, inorder);
}