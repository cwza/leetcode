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
};


class Solution {
// Binary Search, Time: O(h), Space: O(1)
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if(p->val > q->val) swap(p, q);
        while(root) {
            if(root->val > q->val) {
                root = root->left;
            } else if(root-> val < p->val) {
                root = root->right;
            } else {
                return root;
            }
        }
        return nullptr;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    
}