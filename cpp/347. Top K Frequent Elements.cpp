#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

// class Solution {
// // QuickSelect by STL, Time: O(n), Space: O(n)
// public:
//     vector<int> topKFrequent(vector<int>& nums, int k) {
//         unordered_map<int, int> counter;       
//         for(int num : nums) counter[num]++;
//         vector<pi> data(counter.begin(), counter.end()); // [(num, freq), ...]

//         auto comp = [](pi &lhs, pi &rhs) {
//             return lhs.second > rhs.second;
//         };
//         nth_element(data.begin(), data.begin()+k-1, data.end(), comp);

//         vi ans;
//         for(int i = 0; i < k; i++) ans.push_back(data[i].first);
//         return ans;
//     }
// };

class Solution {
// Quick Select, Time: O(n), Space: O(n)
public:
    int partition(vector<pi> &data, int left, int right) {
        int i = left, j = right;
        while(i != j) {
            while(data[j].second > data[left].second && i < j) j--;
            while(data[i].second <= data[left].second && i < j) i++;
            if(i < j) swap(data[i], data[j]);
        }
        swap(data[left], data[i]);
        return i;
    }
    void quickSelect(vector<pi> &data, int left, int right, int k) {
        if(left >= right) return;

        int pivotIdx = partition(data, left, right);
        if(pivotIdx == k) return;
        else if(pivotIdx > k) quickSelect(data, left, pivotIdx-1, k);
        else quickSelect(data, pivotIdx+1, right, k);
    }
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> counter;    
        for(int num : nums) counter[num]++;
        vector<pi> data(counter.begin(), counter.end()); // [(num, freq), ...]
        int n = data.size();

        quickSelect(data, 0, data.size()-1, n-k);

        vi ans;
        for(int i = n-1; i >= 0 && k--; i--) ans.push_back(data[i].first);
        return ans;
    }
    void printData(vector<pi> data) {
        for(auto [num, freq] : data) cout << num << ":" << freq << " ";
        cout << endl;
    }
};

// class Solution {
// // Bucket Sort because frequency is never greater than n, Time: O(n), Space: O(n)
// public:
//     vector<int> topKFrequent(vector<int>& nums, int k) {
//         int n = nums.size();
//         unordered_map<int, int> counter;       
//         for(int num : nums) counter[num]++;
//         vvi bucket(n+1, vi());

//         for(auto [num, freq] : counter) bucket[freq].push_back(num);

//         vi ans;
//         for(int i = n; i >= 0 && k > 0; i--) {
//             for(int num : bucket[i]) {
//                 ans.push_back(num);
//                 k--;
//             }
//         }
//         return ans;
//     }
// };

void printAns(vi ans) {
    for(int num : ans) cout << num << " ";
    cout << "\n";
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; vi nums; int k; vi ans;

    nums = {1,1,1,2,2,3}; k = 2;
    ans = solution.topKFrequent(nums, k);
    printAns(ans); // [1,2]

    nums = {1}; k = 1;
    ans = solution.topKFrequent(nums, k);
    printAns(ans); // [1]
}