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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode dummy;
        dummy.next = head;
        ListNode *l = &dummy, *r = &dummy;       
        for(int i = 0; i < n+1; i++) r = r->next;
        while(r) {
            l = l->next;
            r = r->next;
        }
        l->next = l->next->next;
        return dummy.next;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    
}