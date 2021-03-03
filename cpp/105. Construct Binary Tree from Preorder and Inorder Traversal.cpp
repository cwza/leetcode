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
    TreeNode* helper(int preStart, int inStart, int inEnd, vi &preorder, vi &inorder, unordered_map<int, int> &numToIdx) {
        if(inEnd < inStart) return nullptr;
        TreeNode *node = new TreeNode(preorder[preStart]);
        int mid = numToIdx[node->val];
        node->left = helper(preStart+1, inStart, mid-1, preorder, inorder, numToIdx);
        node->right = helper(preStart+mid-inStart+1, mid+1, inEnd, preorder, inorder, numToIdx);
        return node;
    }
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        unordered_map<int, int> numToIdx;
        for(int i = 0; i < inorder.size(); i++) numToIdx[inorder[i]] = i;
        return helper(0, 0, inorder.size()-1, preorder, inorder, numToIdx);
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