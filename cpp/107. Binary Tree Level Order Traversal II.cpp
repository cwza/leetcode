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
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        if(!root) return vvi();
        queue<TreeNode*> q; q.push(root);
        vvi ans;
        while(!q.empty()) {
            int sz = q.size();
            ans.push_back(vi(sz));
            for(int i = 0; i < sz; i++) {
                TreeNode *node = q.front(); q.pop();
                ans.back()[i] = node->val;
                if(node->left) q.push(node->left);
                if(node->right) q.push(node->right);
            }
        }
        reverse(ans.begin(), ans.end());
        return ans;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    TreeNode *root = new TreeNode();
    Solution solution;
    vvi ans = solution.levelOrderBottom(root);
    for(auto l : ans) {
        cout << "[ ";
        for(auto num : l) {
            cout << num << " ";
        }
        cout << " ]";
    }
}