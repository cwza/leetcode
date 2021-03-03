#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

/*
Key: The answer is equal to the centroids of this graph and the number of this tree-like graph is no more than 2.
Q: How to find centroids??
Alg:
1. Find all leaves(outdegree is 1)
2. Remove them from graph
3. Repeat until the nodes in graph is less than or equel to 2
4. Return the remained nodes 

The process is very like the topological sort, but instead of remove indegree 0 nodes we remove outdegree 1 nodes.
For topological sort, refer to Leetcode 210
*/

class Solution {
// Time: O(V), Space: O(V)
public:
    vector<int> findMinHeightTrees(int n, vector<vector<int>>& edges) {
        if(n==1) return vi({0});       
        if(n==2) return vi({0,1});       

        // Build Graph
        vvi graph(n, vi());
        for(vi edge : edges) {
            int a = edge[0], b = edge[1];
            graph[a].push_back(b);
            graph[b].push_back(a);
        }

        // Count #outdegree of each node and initialize queue to nodes that #outdegree is 1(leaf)
        int outdegree[n];
        queue<int> q;
        for(int node = 0; node < n; node++) {
            int numOutdegree = graph[node].size();
            outdegree[node] = numOutdegree;
            if(numOutdegree==1) q.push(node);
        }

        // BFS
        int remainNodes = n;
        while(remainNodes > 2) {
            int qSize = q.size();
            for(int i = 0; i < qSize; i++) {
                int node = q.front(); q.pop();
                remainNodes--; // Remove this node
                outdegree[node]--; // Decrease node's outdegree
                for(int adj : graph[node]) {
                    outdegree[adj]--; // Decrease adj's outdegree
                    if(outdegree[adj]==1) q.push(adj); // If adj's outdegree becomes 1, add it to queue
                }
            }
        }

        // The remaining nodes in queue are answer
        vi ans;
        while(q.size()) {
            ans.push_back(q.front()); 
            q.pop();
        }
        return ans;
    }
};

void printAns(vi ans) {
    for(int num : ans) cout << num << " ";
    cout << endl;
}

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; int n; vvi edges; vi ans;

    n = 4; edges = {{1,0},{1,2},{1,3}};
    ans = solution.findMinHeightTrees(n, edges);
    printAns(ans);
    
    n = 6; edges = {{3,0},{3,1},{3,2},{3,4},{5,4}};
    ans = solution.findMinHeightTrees(n, edges);
    printAns(ans);

    n = 1; edges = {};
    ans = solution.findMinHeightTrees(n, edges);
    printAns(ans);

    n = 2; edges = {{0,1}};
    ans = solution.findMinHeightTrees(n, edges);
    printAns(ans);
}