#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

// class Trie {
// private:
//     class TrieNode {
//     public:
//         bool isEnd = false;
//         unordered_map<char, TrieNode*> links;
//         TrieNode(){}
//     };
// public:
//     /** Initialize your data structure here. */
//     TrieNode *root;
//     Trie() {
//         root = new TrieNode();
//     }
//     /** Inserts a word into the trie. */
//     void insert(string word) {
//         TrieNode *cur = root;
//         for(char ch : word) {
//             if(!cur->links.count(ch)) cur->links[ch] = new TrieNode();
//             cur = cur->links[ch];
//         }
//         cur->isEnd = true;
//     }
//     /** Returns if the word is in the trie. */
//     bool search(string word) {
//         TrieNode *cur = root;
//         for(char ch : word) {
//             if(!cur->links.count(ch)) return false;
//             cur = cur->links[ch];
//         }
//         return cur->isEnd;
//     }
//     /** Returns if there is any word in the trie that starts with the given prefix. */
//     bool startsWith(string prefix) {
//         TrieNode *cur = root;
//         for(char ch : prefix) {
//             if(!cur->links.count(ch)) return false;
//             cur = cur->links[ch];
//         }
//         return true;
//     }
// };

// class Trie {
// // Add Destroctor
// private:
//     class TrieNode {
//     public:
//         bool isEnd = false;
//         unordered_map<char, TrieNode*> links;
//         TrieNode(){}
//     };
// public:
//     /** Initialize your data structure here. */
//     TrieNode *root;
//     vector<TrieNode*> allNodes;
//     Trie() {
//         root = new TrieNode();
//         allNodes.push_back(root);
//     }
//     ~Trie() {
//         for(TrieNode *&node : allNodes) delete node;
//     }
//     /** Inserts a word into the trie. */
//     void insert(string word) {
//         TrieNode *cur = root;
//         for(char ch : word) {
//             if(!cur->links.count(ch)) {
//                 cur->links[ch] = new TrieNode();
//                 allNodes.push_back(cur->links[ch]);
//             }
//             cur = cur->links[ch];
//         }
//         cur->isEnd = true;
//     }
//     /** Returns if the word is in the trie. */
//     bool search(string word) {
//         TrieNode *cur = root;
//         for(char ch : word) {
//             if(!cur->links.count(ch)) return false;
//             cur = cur->links[ch];
//         }
//         return cur->isEnd;
//     }
//     /** Returns if there is any word in the trie that starts with the given prefix. */
//     bool startsWith(string prefix) {
//         TrieNode *cur = root;
//         for(char ch : prefix) {
//             if(!cur->links.count(ch)) return false;
//             cur = cur->links[ch];
//         }
//         return true;
//     }
// };

class Trie {
// Manage TrieNode by unique_ptr thus we don't have to add destructor
private:
    class TrieNode {
    public:
        bool isEnd = false;
        unordered_map<char, unique_ptr<TrieNode>> links;
        TrieNode(){}
    };
public:
    /** Initialize your data structure here. */
    unique_ptr<TrieNode> root;
    Trie() {
        root = make_unique<TrieNode>();
    }
    /** Inserts a word into the trie. */
    void insert(string word) {
        TrieNode*  cur = root.get();
        for(char ch : word) {
            if(!cur->links.count(ch)) cur->links[ch] = make_unique<TrieNode>();
            cur = cur->links[ch].get();
        }
        cur->isEnd = true;
    }
    /** Returns if the word is in the trie. */
    bool search(string word) {
        TrieNode *cur = root.get();
        for(char ch : word) {
            if(!cur->links.count(ch)) return false;
            cur = cur->links[ch].get();
        }
        return cur->isEnd;
    }
    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix) {
        TrieNode *cur = root.get();
        for(char ch : prefix) {
            if(!cur->links.count(ch)) return false;
            cur = cur->links[ch].get();
        }
        return true;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Trie trie;
    trie.insert("apple");
    assert(trie.search("apple")==true);   // returns true
    assert(trie.search("app")==false);     // returns false
    assert(trie.startsWith("app")==true); // returns true
    trie.insert("app");   
    assert(trie.search("app")==true);     // returns true
}