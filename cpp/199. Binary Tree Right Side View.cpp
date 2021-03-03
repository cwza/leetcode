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
    vector<int> rightSideView(TreeNode* root) {
        if(!root) return vi();       
        queue<TreeNode*> q; q.push(root);
        vi ans;
        while(q.size()) {
            int qSize = q.size();
            for(int i = 0; i < qSize; i++) {
                TreeNode* node = q.front(); 
                q.pop();
                if(i==0) ans.push_back(node->val);
                if(node->right) q.push(node->right);
                if(node->left) q.push(node->left);
            }
        }
        return ans;
    }
};

#include<fmt/core.h>
#include<fmt/ranges.h>
using namespace fmt;
int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    TreeNode *l = new TreeNode(2);
    TreeNode *r = new TreeNode(3);
    TreeNode *root = new TreeNode(1, l, r);
    Solution solution;
    vi ans = solution.rightSideView(root);
    print("{}\n", ans);
}