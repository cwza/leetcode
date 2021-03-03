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
// Prefixsum, Time: O(n), Space: O(n)
// Concept is same as LeetCode 560
public:
    void dfs(TreeNode *root, int runningSum, int sum, unordered_map<int, int> &counter, int &ans) {
        if(!root) return;
        runningSum += root->val;
        if(runningSum == sum) ans++;
        if(counter.count(runningSum-sum)) ans += counter[runningSum-sum];
        counter[runningSum]++;
        dfs(root->left, runningSum, sum, counter, ans);
        dfs(root->right, runningSum, sum, counter, ans);
        counter[runningSum]--;
    }
    int pathSum(TreeNode* root, int sum) {
        unordered_map<int, int> counter;
        int ans = 0;
        dfs(root, 0, sum, counter, ans);
        return ans;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    TreeNode *lll = new TreeNode(3);
    TreeNode *llr = new TreeNode(-2);
    TreeNode *ll = new TreeNode(3, lll, llr);
    TreeNode *lrr = new TreeNode(1);
    TreeNode *lr = new TreeNode(2, nullptr, lrr);
    TreeNode *l = new TreeNode(5, ll, lr);
    TreeNode *rr = new TreeNode(11);
    TreeNode *r = new TreeNode(-3, nullptr, rr);
    TreeNode *root = new TreeNode(10, l, r);
    Solution solution;
    int ans = solution.pathSum(root, 8);
    assert(ans==3);
}