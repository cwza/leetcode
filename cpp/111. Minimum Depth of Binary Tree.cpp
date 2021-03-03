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
// DFS, Time: O(n), Space: O(n)
public:
    int minDepth(TreeNode* root) {
        if(!root) return 0;
        if(!root->left && !root->right) return 1;
        if(!root->left) return 1 + minDepth(root->right);
        if(!root->right) return 1 + minDepth(root->left);
        return 1 + min(minDepth(root->left), minDepth(root->right));
    }
};

class Solution {
// BFS, Time: O(n), Space: O(n)
public:
    int minDepth(TreeNode* root) {
        if(!root) return 0;
        queue<TreeNode*> q; q.push(root);
        int ans = 0;
        bool is_terminal = false;
        while(!q.empty() && !is_terminal) {
            int sz = q.size();
            ans += 1;
            for(int i = 0; i < sz; i++) {
                TreeNode *node = q.front(); q.pop();
                if(!node->left && !node->right) return ans;
                if(node->left) q.push(node->left);
                if(node->right) q.push(node->right);
            }
        }
        return -1;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    
}