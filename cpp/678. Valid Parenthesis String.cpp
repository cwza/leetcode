#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define ar array

class Solution {
public:
    bool checkValidString(string s) {
        // Check from left that number of ')' is always less than or equal to number of '(' or '*'
        int numl = 0;
        for(char ch : s) {
            if(ch==')') {
                if(numl==0) return false;
                numl--;
            } else {
                numl++;
            }
        }
        // Check from right that number of '(' is always less than or equal to number of ')' or '*'
        int numr = 0;
        for(int i = s.size()-1; i >= 0; --i) {
            char ch = s[i];
            if(ch=='(') {
                if(numr==0) return false;
                numr--;
            } else {
                numr++;
            }
        }
        return true;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);
    // freopen("input.txt", "r", stdin); 
    // freopen("output.txt", "w", stdout);
}