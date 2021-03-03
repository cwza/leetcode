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
// Time: O(mn)
public:
    bool isSameTree(TreeNode* s, TreeNode* t) {
        if(!s && !t) return true;
        if((s && !t) || (!s && t)) return false;
        return s->val==t->val && isSameTree(s->left, t->left) && isSameTree(s->right, t->right);
    }
    bool isSubtree(TreeNode* s, TreeNode* t) {
        if((s && !t) || (!s && t)) return isSameTree(s, t);
        return isSameTree(s, t) || isSubtree(s->left, t) || isSubtree(s->right, t);
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    
}