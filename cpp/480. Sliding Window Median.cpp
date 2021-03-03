#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;
typedef set<pi>::iterator si;

/*
Please refer to LeetCode 295
*/

class Solution {
// Balanced Binary Search Tree
public:
    set<pi> s; // {(value, index)}
    si mIter;
    double getMedian() {
        if(s.size()%2) return (*mIter).first;
        else return ((double)(*mIter).first + (*next(mIter)).first) / 2;
    }
    void add(pi newElem) {
        auto [iter, _] = s.insert(newElem);
        if(s.size()==1) {
            mIter = iter;
            return;
        }
        if(s.size()%2) {
            if(newElem > *mIter) mIter++;
        } else {
            if(newElem < *mIter) mIter--;
        }
    }
    void remove(pi remElem) {
        if(s.size()%2) {
            if(remElem >= *mIter) mIter--;
        } else {
            if(remElem <= *mIter) mIter++;
        }
        s.erase(remElem); // We don't need to find because the element we store are unique
        // s.erase(s.find(remElem));
    }
    vector<double> medianSlidingWindow(vector<int>& nums, int k) {
        int n = nums.size();
        vector<double> ans;
        for(int i = 0; i < n; ++i) {
            auto newElem = make_pair(nums[i], i);
            add(newElem);
            if(i == k-1) ans.push_back(getMedian());
            if(i >= k) {
                auto remElem = make_pair(nums[i-k], i-k);
                remove(remElem);
                ans.push_back(getMedian());
            }
        }
        return ans;
    }
};

// class Solution {
// // Less Heap + Larger Heap
// public:
//     set<pi, greater<pi>> less; // as Max Heap, store {(value, index)}
//     set<pi> larger; // as Min Heap
//     double getMedian() {
//         si lessTop = less.begin();
//         si largerTop = larger.begin();
//         if((less.size()+larger.size())%2) return (*lessTop).first;
//         else return ((double)(*lessTop).first+ (*largerTop).first)  / 2;
//     }
//     void balance() {
//         if(larger.size() > less.size()) {
//             less.insert(*larger.begin());
//             larger.erase(larger.begin());
//         }
//         if(less.size() >= larger.size() + 2) {
//             larger.insert(*less.begin());
//             less.erase(less.begin());
//         }
//     }
//     void add(pi newElem) {
//         if(less.size()==0 || newElem <= *less.begin()) less.insert(newElem);
//         else larger.insert(newElem);
//         balance();
//     }
//     void remove(pi remElem) {
//         if(remElem <= *less.begin()) less.erase(remElem);
//         else larger.erase(remElem);
//         balance();
//     }
//     vector<double> medianSlidingWindow(vector<int>& nums, int k) {
//         int n = nums.size();
//         vector<double> ans;
//         for(int i = 0; i < n; ++i) {
//             pi newElem = make_pair(nums[i], i);
//             add(newElem);
//             if(i==k-1) ans.push_back(getMedian());
//             if(i>=k) {
//                 pi remElem = make_pair(nums[i-k], i-k);
//                 remove(remElem);
//                 ans.push_back(getMedian());
//             }
//         }
//         return ans;
//     }
// };

#include<fmt/core.h>
#include<fmt/ranges.h>
using namespace fmt;

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; vi nums; int k; vector<double> ans;

    solution = Solution();
    nums = {1,3,-1,-3,5,3,6,7}; k = 3;
    ans = solution.medianSlidingWindow(nums, k);
    print("{}\n", ans);
    assert(ans==vector<double>({1,-1,-1,3,5,6}));
}