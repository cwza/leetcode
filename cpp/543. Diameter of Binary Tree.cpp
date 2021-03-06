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
    int ans = 0;
    int dfs(TreeNode *root) { // return the depth of root
        int d = 0, dd = 0;
        if(root->left) {
            int d1 = dfs(root->left);
            dd += d1+1;
            d = max(d, d1+1);
        }
        if(root->right) {
            int d2 = dfs(root->right);
            dd += d2+1;
            d = max(d, d2+1);
        }
        ans = max(ans, dd);
        return d;
    }
    int diameterOfBinaryTree(TreeNode* root) {
        dfs(root);
        return ans;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    
}