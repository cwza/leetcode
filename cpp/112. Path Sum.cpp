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
    bool hasPathSum(TreeNode* root, int sum) {
        if(!root) return false;
        int remain = sum - root->val;   
        if(!root->left && !root->right) {
            if(remain == 0) return true;
            return false;
        }
        if(hasPathSum(root->left, remain)) return true;
        if(hasPathSum(root->right, remain)) return true;
        return false;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    
}