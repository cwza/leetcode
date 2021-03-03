#include <fmt/core.h>
#include <fmt/ranges.h>
using namespace fmt;

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
    TreeNode(int x, TreeNode *l, TreeNode *r) : val(x), left(l), right(r) {}
};

// class Solution {
// // Build Graph + BFS, Time: O(n), Space: O(n)
// public:
//     void dfs(TreeNode* root, unordered_map<int, vi> &graph) {
//         if(root->left) {
//             graph[root->val].push_back(root->left->val);
//             graph[root->left->val].push_back(root->val);
//             dfs(root->left, graph);
//         }
//         if(root->right) {
//             graph[root->val].push_back(root->right->val);
//             graph[root->right->val].push_back(root->val);
//             dfs(root->right, graph);
//         }
//     }
//     vector<int> distanceK(TreeNode* root, TreeNode* target, int K) {
//         // Build Graph
//         unordered_map<int, vi> graph;
//         dfs(root, graph);

//         // Run BFS
//         queue<int> q; q.push(target->val);
//         int level = 0;
//         vi ans;
//         unordered_set<int> visited;
//         while(q.size() && level <= K) {
//             int qSize = q.size();
//             for(int i = 0; i < qSize; i++) {
//                 int node = q.front(); q.pop();
//                 visited.insert(node);
//                 if(level==K) ans.push_back(node);
//                 for(int adj : graph[node]) {
//                     if(!visited.count(adj)) q.push(adj);
//                 }
//             }
//             level++;
//         }
//         return ans;
//     }
// };

class Solution {
public:
    void collect(TreeNode *root, int dist, vi &ans) {
        // add nodes to ans. add which nodes?? distance between root and node is dist and those nodes are under the root.
        if(dist < 0 || !root) return;
        if(dist==0) {
            ans.push_back(root->val);
            return;
        }
        collect(root->left, dist-1, ans);
        collect(root->right, dist-1, ans);
    }
    int helper(TreeNode *root, TreeNode* target, vector<tuple<TreeNode*, int, bool>> &table) {
        // Save the distance from all node to target into table, only dist >= 0 will be saved 
        // table: [ (node, dist to target, is target in left tree of node) ]
        if(!root) return -1;
        if(root==target) {
            table.push_back(make_tuple(root, 0, true));
            return 0;
        }
        int lDist = helper(root->left, target, table);
        int rDist = helper(root->right, target, table);
        if(lDist >= 0) {
            table.push_back(make_tuple(root, lDist+1, true));
            return lDist + 1;
        }
        if(rDist >= 0) {
            table.push_back(make_tuple(root, rDist+1, false));
            return rDist + 1;
        }
        return -1;
    }
    vector<int> distanceK(TreeNode* root, TreeNode* target, int K) {
        vector<tuple<TreeNode*, int, bool>> table;
        helper(root, target, table);
        vi ans;
        for(auto [node, dist, isTargetLeft] : table) {
            // cout << node->val << " " << dist << " " << isTargetLeft << endl;
            if(dist==K) ans.push_back(node->val);
            else if(dist==0) collect(node, K, ans);
            else if(isTargetLeft) collect(node->right, K-dist-1, ans);
            else if(!isTargetLeft) collect(node->left, K-dist-1, ans);
        }
        return ans;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    TreeNode *l = new TreeNode(5);
    TreeNode *r = new TreeNode(1);
    TreeNode *root = new TreeNode(3, l, r);

    Solution solution; vi ans;
    ans = solution.distanceK(root, root, 1);
    print("{}\n", ans);
}