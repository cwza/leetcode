#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define ar array

class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        while(stones.size()>1) {
            sort(stones.begin(), stones.end());
            int v = stones.back() - stones[stones.size()-2];
            stones.pop_back();
            stones.pop_back();
            if(v!=0) stones.push_back(v);
        }
        if(stones.size()==0) return 0;
        return stones[0];
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);
    // freopen("input.txt", "r", stdin); 
    // freopen("output.txt", "w", stdout);
}