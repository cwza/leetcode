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
    ListNode* removeElements(ListNode* head, int val) {
        if(!head) return head;       

        ListNode dummy = ListNode(0);
        dummy.next = head;
        ListNode *pre = &dummy, *cur = head;

        while(cur) {
            if(cur->val == val) {
                pre->next = cur->next;
                delete cur;
                cur = pre->next;
            } else {
                pre = pre->next;
                cur = cur->next;
            }
        }
        return dummy.next;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    
}