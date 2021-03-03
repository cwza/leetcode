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
// BFS + Heap index, Time: O(n), Space: O(n)
public:
    int widthOfBinaryTree(TreeNode* root) {
        queue<pair<TreeNode*, int>> q; q.push(make_pair(root, 1));       
        int ans = 0;
        while(q.size()) {
            int qSize = q.size();
            int first = -1, last = -1;
            int offset = q.front().second;
            for(int i = 0; i < qSize; i++) {
                auto [node, number] = q.front(); q.pop();
                if(i == 0) first = number;
                else if(i == qSize-1) last = number;
                if(node->left) q.push(make_pair(node->left, 2*(number-offset)));
                if(node->right) q.push(make_pair(node->right, 2*(number-offset)+1));
            }
            if(last == -1) ans = max(ans, 1);
            else ans = max(ans, last-first+1);
        }
        return ans;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    
}