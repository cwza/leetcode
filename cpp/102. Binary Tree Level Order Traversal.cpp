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
// BFS, Time: O(n), Space: O(n)
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        if(!root) return vvi();
        queue<TreeNode*> q; q.push(root);
        vvi ans;
        while(q.size()) {
            int qSize = q.size();
            ans.push_back(vi(qSize));
            vi &last = ans.back();
            for(int i = 0; i < qSize; i++) {
                TreeNode *node = q.front(); q.pop();
                last[i] = node->val;
                if(node->left) q.push(node->left);
                if(node->right) q.push(node->right);
            }
        }
        return ans;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

}