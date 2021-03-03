#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;


struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
// Floyd’s algorithm, Time: O(n), Space: O(1)
public:
    bool hasCycle(ListNode *head) {
        ListNode *slow = head, *fast = head;       
        while(fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
            if(fast==slow) return true;
        }
        return false;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    
}