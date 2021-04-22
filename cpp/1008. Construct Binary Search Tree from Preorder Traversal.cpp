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

// Naive, O(n^2)
// class Solution {
// public:
//     TreeNode* dfs(int i, int j, vector<int> &preorder) {
//         TreeNode *root = new TreeNode(preorder[i]);
//         int kk = j+1;
//         for(int k = i+1; k <= j; ++k) {
//             if(preorder[k]>preorder[i]) {
//                 kk = k;
//                 break;
//             }
//         }
//         if(i+1 <= kk-1) root->left = dfs(i+1, kk-1, preorder);
//         if(kk<=j) root->right = dfs(kk, j, preorder);
//         return root;
//     }
//     TreeNode* bstFromPreorder(vector<int>& preorder) {
//         int n = preorder.size();
//         return dfs(0, n-1, preorder);
//     }
// };

// Use inorder, O(nlogn)
// Just like Leetcode 105
// class Solution {
// public:
//     vector<int> pre, in;
//     int prei = 0;
//     TreeNode* dfs(int ini, int inj) {
//         int rootval = pre[prei];
//         prei++;
//         TreeNode *root = new TreeNode(rootval);
//         auto iter = lower_bound(in.begin()+ini, in.begin()+inj+1, rootval);
//         int k = iter-in.begin();
//         if(ini <= k-1) root->left = dfs(ini, k-1);
//         if(k+1 <= inj) root->right = dfs(k+1, inj);
//         return root;
//     }
//     TreeNode* bstFromPreorder(vector<int>& preorder) {
//         pre = preorder;
//         in = preorder; sort(in.begin(), in.end());
//         return dfs(0, in.size()-1);
//     }
// };

// O(n)
// https://www.youtube.com/watch?v=RyAGEb4VWo0
class Solution {
public:
    vector<int> pre;
    int prei = 0;
    TreeNode* dfs(int limit) {
        if(prei>=pre.size() || pre[prei] > limit) return nullptr;
        int rootval = pre[prei];
        prei++;
        TreeNode *root = new TreeNode(rootval);
        root->left = dfs(rootval);
        root->right = dfs(limit);
        return root;
    }
    TreeNode* bstFromPreorder(vector<int>& preorder) {
        pre = preorder;
        return dfs(1e9);
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);
    // freopen("input.txt", "r", stdin); 
    // freopen("output.txt", "w", stdout);

}