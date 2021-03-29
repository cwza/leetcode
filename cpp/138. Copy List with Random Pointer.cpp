#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};

class Solution {
public:
    Node* copyRandomList(Node* head) {
        if(!head) return head;
        map<Node*, Node*> m;
        Node *cur = head;
        Node *newNode = new Node(cur->val);
        m[cur] = newNode;
        while(cur->next) {
            newNode->next = new Node(cur->next->val);
            m[cur->next] = newNode->next;
            cur = cur->next;
            newNode = newNode->next;
        }
        cur = head;
        newNode = m[head];
        while(cur) {
            if(cur->random==nullptr) newNode->random = nullptr;
            else newNode->random = m[cur->random];
            cur = cur->next;
            newNode = newNode->next;
        }
        return m[head];
    }
};


int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    auto node1 = Node(1);
    auto node2 = Node(2);
    node1.next = &node2;
    node1.random = &node2;
    node2.random = &node2;

    Solution solution;
    solution.copyRandomList(&node1);

    cout << "Hello";
}