#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};

class Solution {
public:
    Node* dfs(Node *ori, unordered_map<int, Node*> &table) {
        if(!ori) return ori;
        auto tmp = table.find(ori->val);
        if(tmp != table.end()) return (*tmp).second;

        Node *clone = new Node(ori->val);
        table[ori->val] = clone;
        for(Node* adj : ori->neighbors) {
            clone->neighbors.push_back(dfs(adj, table));
        }
        return clone;
    }
    Node* cloneGraph(Node* node) {
        unordered_map<int, Node*> table;
        return dfs(node, table);
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    
}