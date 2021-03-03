#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

// class Solution {
// // MaxHeap, Time: O(nlogk), Space: O(k)
// public:
//     vector<vector<int>> kClosest(vector<vector<int>>& points, int K) {
//         auto comp = [](vi &lhs, vi &rhs) {
//             return lhs[0]*lhs[0]+lhs[1]*lhs[1] <= rhs[0]*rhs[0]+rhs[1]*rhs[1];
//         };
//         priority_queue<vi, vvi, decltype(comp)> pq(comp); 

//         for(vi point : points) {
//             pq.push(point);
//             if(pq.size() > K) pq.pop();
//         }

//         vvi ans;
//         while(pq.size()) {
//             ans.push_back(pq.top()); 
//             pq.pop();
//         }
//         return ans;
//     }
// };

// class Solution {
// // MinHeap, Time: O(n+klogn), Space: O(n)
// public:
//     vector<vector<int>> kClosest(vector<vector<int>>& points, int K) {
//         auto comp = [](vi &lhs, vi &rhs) {
//             return lhs[0]*lhs[0]+lhs[1]*lhs[1] > rhs[0]*rhs[0]+rhs[1]*rhs[1];
//         };
//         priority_queue<vi, vvi, decltype(comp)> pq(points.begin(), points.end(), comp); // Heapify, O(n)

//         vvi ans;
//         while(K--) {
//             ans.push_back(pq.top()); 
//             pq.pop();
//         }
//         return ans;
//     }
// };

// class Solution {
// // QuickSelect by STL, Time: O(n), Space: O(1)
// public:
//     vector<vector<int>> kClosest(vector<vector<int>>& points, int K) {
//         auto comp = [](vi &lhs, vi &rhs) {
//             return lhs[0]*lhs[0]+lhs[1]*lhs[1] < rhs[0]*rhs[0]+rhs[1]*rhs[1];
//         };
//         nth_element(points.begin(), points.begin()+K-1, points.end(), comp);
//         return vvi(points.begin(), points.begin()+K);
//     }
// };

class Solution {
// QuickSelect, Time: O(n), Space: O(1)
public:
    int partition(vvi &points, int left, int right) {
        auto dist = [](vi &point) {
            return point[0]*point[0] + point[1]*point[1];
        };
        int i = left;
        int j = right;
        while(i != j) {          
            while(dist(points[j]) > dist(points[left]) && i < j) j--;
            while(dist(points[i]) <= dist(points[left]) && i < j) i++;
            if(i < j) swap(points[i], points[j]);
        }
        swap(points[left], points[i]);
        return i;
    }
    void quickSelect(vvi &points, int left, int right, int k) {
        if(left >= right) return;

        int pivot = rand() % (right - left + 1) + left;
        swap(points[left], points[pivot]);

        int pivotIdx = partition(points, left, right);
        if(pivotIdx == k) return;
        else if(pivotIdx > k) quickSelect(points, left, pivotIdx-1, k);
        else quickSelect(points, pivotIdx+1, right, k);
    }
    vector<vector<int>> kClosest(vector<vector<int>>& points, int K) {
        quickSelect(points, 0, points.size()-1, K-1);
        return vvi(points.begin(), points.begin()+K);
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; vvi points; int K; vvi ans;

    points = {{1,3},{-2,2}};
    K = 1;
    ans = solution.kClosest(points, K);
    assert(ans==vvi({{-2,2}}));

    points = {{3,3},{5,-1},{-2,4}};
    K = 2;
    ans = solution.kClosest(points, K);
    // assert(ans==vvi({{-2,4},{3,3}}));
    assert(ans==vvi({{3,3},{-2,4}}));
}