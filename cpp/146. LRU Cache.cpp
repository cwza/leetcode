#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

class LRUCache {
public:
    int capacity = 0;
    unordered_map<int, list<pi>::iterator> dict;  // {key: iter, ...}
    list<pi> li; // [(key, val), ...]
    LRUCache(int capacity):capacity(capacity) {}
    int get(int key) {
        if(!dict.count(key)) return -1;
        auto iter = dict[key];
        li.push_front(*iter);
        li.erase(iter);
        dict[key] = li.begin();
        return li.front().second;
    }
    void put(int key, int value) {
        if(dict.count(key)) {
            auto iter = dict[key];
            li.push_front(make_pair(key, value));
            li.erase(iter);
            dict[key] = li.begin();
        } else {
            if(dict.size() < capacity) {
                li.push_front(make_pair(key, value));
                dict[key] = li.begin();
            } else {
                dict.erase(li.back().first);
                li.pop_back();
                li.push_front(make_pair(key, value));
                dict[key] = li.begin();
            }
        }
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