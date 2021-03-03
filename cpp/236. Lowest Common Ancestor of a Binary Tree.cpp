#include <fmt/core.h>
#include <fmt/ranges.h>
using namespace fmt;

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
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
    TreeNode(int x, TreeNode* l, TreeNode *r) : val(x), left(l), right(r) {}
};

class Solution {
// DFS to get parent and follow it to get LCA.
public:
    void dfs(TreeNode *root, int depth, unordered_map<int, TreeNode*> &parent, pi &depths, TreeNode *p, TreeNode *q) {
        // depths: (depth of p, depth of q), parent: {node_val: its parent}
        if(depths.first && depths.second) return;
        if(root == p) depths.first = depth;
        if(root == q) depths.second = depth;
        if(root->left) {
            parent[root->left->val] = root;
            dfs(root->left, depth+1, parent, depths, p, q);
        }
        if(root->right) {
            parent[root->right->val] = root;
            dfs(root->right, depth+1, parent, depths, p, q);
        }
    } 
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        unordered_map<int, TreeNode*> parent;
        pi depths;
        dfs(root, 1, parent, depths, p, q); // Get parent and depths
        // put p and q to the same depth
        if(depths.first > depths.second) {
            int diff = depths.first - depths.second;
            while(diff--) p = parent[p->val];
        } else {
            int diff = depths.second - depths.first;
            while(diff--) q = parent[q->val];
        }
        // move p, q together to get their first meet parent
        while(p != q) {
            p = parent[p->val];
            q = parent[q->val];
        }
        return p;
    }
    void printParent(unordered_map<int, TreeNode*> parent) {
        for(auto [nodeVal, parent] : parent) {
            cout << nodeVal << ":" << parent->val << " ";
        }
        cout << endl;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    TreeNode *ll = new TreeNode(6);
    TreeNode *lrl = new TreeNode(7);
    TreeNode *lrr = new TreeNode(4);
    TreeNode *lr = new TreeNode(2, lrl, lrr);
    TreeNode *l = new TreeNode(5, ll, lr);
    TreeNode *r = new TreeNode(1);
    TreeNode *root = new TreeNode(3, l, r);

    Solution solution;
    TreeNode *ans = solution.lowestCommonAncestor(root, l, lrr);
    cout << ans->val << endl;
}