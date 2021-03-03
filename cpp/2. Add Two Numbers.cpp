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
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int carry = 0;
        ListNode dummy;
        ListNode *cur = &dummy;
        while(l1 || l2) {
            int val = 0;
            if(l1) {
                val += l1->val;
                l1 = l1->next;
            }
            if(l2) {
                val += l2->val;
                l2 = l2->next;
            }
            val += carry;
            int nextVal = val % 10;
            carry = val / 10;
            cur->next = new ListNode(nextVal);
            cur = cur->next;
        }       
        if(carry) cur->next = new ListNode(carry);
        return dummy.next;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    
}