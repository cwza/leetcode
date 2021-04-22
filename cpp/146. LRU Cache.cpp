#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define ar array

// Use queue and map
// class LRUCache {
// public:
//     int cap;
//     int t = 0;
//     map<int, int> mv; // key: val
//     queue<ar<int, 2>> q; // [(key, time)] may have multiple same key but only last is required
//     map<int, int> mt; // key: last time
//     LRUCache(int capacity) {
//         cap = capacity;
//     }
    
//     int get(int key) {
//         if(!mv.count(key)) return -1;
//         q.push({key, t});
//         mt[key] = t++;
//         return mv[key];
//     }
    
//     void put(int key, int value) {
//         if(mv.count(key) || mv.size()<cap) {
//             mv[key] = value;
//             q.push({key, t});
//             mt[key] = t++;
//             return;
//         }
//         while(true) {
//             auto e = q.front(); q.pop();
//             if(e[1]==mt[e[0]]) {
//                 mv.erase(e[0]);
//                 mt.erase(e[0]);
//                 break;
//             }
//         }
//         mv[key] = value;
//         q.push({key, t});
//         mt[key] = t++;
//     }
// };

class LRUCache {
public:
    int cap;
    map<int, list<ar<int, 2>>::iterator> mp; // key: list::iterator
    list<ar<int, 2>> ls; // {key, value}
    LRUCache(int capacity) {
        cap = capacity;
    }
    
    int get(int key) {
        if(!mp.count(key)) return -1;
        auto iter = mp[key];
        int k = (*iter)[0];
        int v = (*iter)[1];
        ls.erase(iter);
        ls.push_back({k, v});
        mp[key] = --ls.end();
        return v;
    }
    
    void put(int key, int value) {
        if(mp.count(key)) {
            auto iter = mp[key];
            int k = (*iter)[0];
            ls.erase(iter);
            ls.push_back({k, value});
            mp[key] = --ls.end();
            return;
        }
        if(mp.size()<cap) {
            ls.push_back({key, value});
            mp[key] = --ls.end();
            return;
        }
        int k = (*ls.begin())[0];
        mp.erase(k);
        ls.erase(ls.begin());
        ls.push_back({key, value});
        mp[key] = --ls.end();
    }
};

#include <fmt/core.h>
#include <fmt/ranges.h>
using namespace fmt;
int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    LRUCache lRUCache(2);
    lRUCache.put(1, 1); // cache is {1=1}
    lRUCache.put(2, 2); // cache is {1=1, 2=2}
    assert(lRUCache.get(1)==1);    // return 1
    lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    assert(lRUCache.get(2)==-1);    // returns -1 (not found)
    lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    assert(lRUCache.get(1)==-1);    // return -1 (not found)
    assert(lRUCache.get(3)==3);    // return 3
    assert(lRUCache.get(4)==4);    // return 4
}