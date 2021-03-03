#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;
typedef set<pi>::iterator si;

/*
https://www.youtube.com/watch?v=60xnYZ21Ir0
*/

// class MedianFinder {
// // Balanced Binary Search Tree
// public:
//     // Space: O(n)
//     set<pi> s; // {(value, index)}
//     si mIter;
//     MedianFinder() {
//     }
//     void addNum(int num) {
//         // Time: O(logn)
//         pi curElem = make_pair(num, s.size());
//         auto [iter, _] = s.insert(curElem);
//         if(s.size() == 1) { // First one
//             mIter = iter;
//             return;
//         }
//         if(s.size()%2) { // odd, after insert
//             if(curElem > *mIter) mIter++;
//         } else { // even, after insert
//             if(curElem < *mIter) mIter--;
//         }
//     }
//     double findMedian() {
//         // Time: O(1)
//         if(s.size()%2) return (*mIter).first; // odd
//         else return ( (double)(*mIter).first + (*next(mIter)).first ) / 2; // even
//     }
// };

class MedianFinder {
// Less Heap + Larger Heap
public:
    // Space: O(n)
    priority_queue<int> less; // Max heap
    priority_queue<int, vi, greater<int>> larger; // Min heap
    MedianFinder() {
    }
    void addNum(int num) {
        // Time: O(logn)
        if(less.size()==0 || num <= less.top()) less.push(num);
        else larger.push(num);

        if(larger.size() > less.size()) {
            less.push(larger.top());
            larger.pop();
        } 
        if(less.size() >= larger.size()+2) {
            larger.push(less.top());
            less.pop();
        }
    }
    double findMedian() {
        // Time: O(1)
        if( (less.size()+larger.size()) % 2 ) return less.top(); // odd
        else return ( (double)less.top() + larger.top() ) / 2; // even
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    MedianFinder mf;

    mf.addNum(1);
    mf.addNum(2);
    cout << mf.findMedian() << endl; // -> 1.5
    mf.addNum(3); 
    cout << mf.findMedian() << endl; // -> 2
}