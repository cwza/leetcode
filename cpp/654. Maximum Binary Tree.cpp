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
// Recursive, Time: O(n^2), Space: O(n)
public:
    TreeNode* helper(vi::iterator start, vi::iterator end) {
        if(start==end) return nullptr;
        vi::iterator maxIter = max_element(start, end); // O(n)
        TreeNode *node = new TreeNode(*maxIter);
        node->left = helper(start, maxIter);
        node->right = helper(maxIter+1, end);
        return node;
    }
    TreeNode* constructMaximumBinaryTree(vector<int>& nums) {
        return helper(nums.begin(), nums.end());
    }
};


// class NumArray {
// private:
//     class SegmentTreeNode {
//     public:
//         int start, end, s, idx;
//         SegmentTreeNode *left, *right;
//         SegmentTreeNode(int start, int end, int s, int idx, SegmentTreeNode* left=nullptr, SegmentTreeNode* right=nullptr)
//         :start(start), end(end), s(s), idx(idx), left(left), right(right){}
//     };
// public:
//     vi nums;
//     SegmentTreeNode *root;
//     NumArray(vi &nums):nums(nums) {
//         root = buildTree(nums);
//     }
//     SegmentTreeNode* buildTree(vi &nums) {
//         function<SegmentTreeNode*(int, int)> helper = [&](int start, int end) -> SegmentTreeNode* {
//             if(end < start) return nullptr;
//             if(start == end) return new SegmentTreeNode(start, end, nums[start], start);
//             int mid = start + (end-start)/2;
//             SegmentTreeNode *left = helper(start, mid);
//             SegmentTreeNode *right = helper(mid+1, end);
//             if(left->s > right->s) return new SegmentTreeNode(start, end, max(left->s, right->s), left->idx, left, right);
//             else return new SegmentTreeNode(start, end, max(left->s, right->s), right->idx, left, right);
//         };
//         return helper(0, nums.size()-1);
//     }
//     pi sumRange(int i, int j) {
//         // return (idx, val), the max element in nums[i, j]
//         function<pi(SegmentTreeNode*, int, int)> helper = [&](SegmentTreeNode* root, int l, int r) {
//             if(root->start == l && root->end == r) return make_pair(root->idx, root->s);
//             int mid = root->start + (root->end-root->start)/2;
//             if(r <= mid) return helper(root->left, l, r);
//             else if(l > mid) return helper(root->right, l, r);
//             auto [lIdx, lVal] = helper(root->left, l, mid);
//             auto [rIdx, rVal] = helper(root->right, mid+1, r);
//             if(lVal > rVal) return make_pair(lIdx, lVal);
//             else return make_pair(rIdx, rVal);
//         };
//         return helper(root, i, j);
//     }
// };

// class Solution {
// // Segment Tree to Find Max in range i, j, Time: O(nlogn), Space: O(n)
// public:
//     TreeNode* helper(int i, int j, NumArray &numArray) {
//         if(i > j) return nullptr;
//         auto [maxIdx, maxElem] = numArray.sumRange(i, j); // O(logn)
//         TreeNode *node = new TreeNode(maxElem);
//         node->left = helper(i, maxIdx-1, numArray);
//         node->right = helper(maxIdx+1, j, numArray);
//         return node;
//     }
//     TreeNode* constructMaximumBinaryTree(vector<int>& nums) {
//         NumArray numArray(nums); // O(n)
//         return helper(0, nums.size()-1, numArray); // O(nlogn)
//     }
// };

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

}