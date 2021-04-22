#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define ar array

/*
push(-2) -> push(0) -> push(-3)
a = [-2, -2, -3] // min value until now
b = [-2, 0, -3] // original stack
*/

class MinStack {
public:
    stack<int> a; // Store the min value till now
    stack<int> b; // Store the original value
    MinStack() {
    }
    void push(int val) {
        b.push(val);
        if(a.size())
            a.push(min(a.top(), val));
        else
            a.push(val);
    }
    void pop() {
        b.pop();
        a.pop();
    }
    int top() {
        return b.top();
    }
    int getMin() {
        return a.top();
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);
    // freopen("input.txt", "r", stdin); 
    // freopen("output.txt", "w", stdout);
    MinStack minStack;
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    cout << minStack.getMin() << "\n"; // return -3
    minStack.pop();
    cout << minStack.top() << "\n";    // return 0
    cout << minStack.getMin() << "\n"; // return -2
}