#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;
typedef vector<double> vd;


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
    vector<double> averageOfLevels(TreeNode* root) {
        if(!root) return vd({0});
        queue<TreeNode*> q; q.push(root);
        vd ans;
        while(!q.empty()) {
            ll total = 0;
            int sz = q.size();
            for(int i = 0; i < sz; i++) {
                TreeNode *node = q.front(); q.pop();
                total += node->val;
                if(node->left) q.push(node->left);
                if(node->right) q.push(node->right);
            }
            ans.push_back((double)total/sz);
        }
        return ans;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    
}