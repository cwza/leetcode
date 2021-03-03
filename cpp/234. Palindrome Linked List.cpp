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
    auto split(ListNode* head) {
        ListNode *fast = head, *slow = head, *pre = nullptr;
        while(fast && fast->next) {
            pre = slow;
            slow = slow->next;
            fast = fast->next->next;
        }
        pre->next = nullptr;
        return pair<ListNode*, ListNode*>(head, slow);
    }
    auto reverse(ListNode* head) {
        ListNode *pre = nullptr, *cur = head, *nxt;
        while(cur) {
            nxt = cur->next;
            cur->next = pre;
            pre = cur;
            cur = nxt;
        }
        return pre;
    }
    bool isPalindrome(ListNode* head) {
        if(!head || !head->next) return true;      
        auto [first, second] = split(head);
        second = reverse(second);

        while(first) {
            if(first->val != second->val) return false;
            first = first->next;
            second = second->next;
        }
        return true;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    
}