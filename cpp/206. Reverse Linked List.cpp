#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;


struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
// Time: O(n), Space: O(1)
public:
    ListNode* reverseList(ListNode* head) {
        if(!head or !head->next) return head;     
        ListNode *cur = head, *pre = nullptr, *nxt;
        while(cur) {
            nxt = cur->next;
            cur->next = pre;
            pre = cur;
            cur = nxt;
        }
        return pre;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    
}