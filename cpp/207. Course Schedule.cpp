#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

void printGraph(vvi &graph) {
    for(int i = 0; i < graph.size(); i++) {
        cout << i << ":";
        for(int adj : graph[i]) {
            cout << adj << " ";
        }
        cout << "\n";
    }
}

class Solution {
// DFS find cycle, Time: O(V+E), Space: O(V)
public:
    bool hasCycle(int node, vi &state, vvi &graph) {
        state[node] = 1;
        for(int adj : graph[node]) {
            if(state[adj]==1) return true;
            if(state[adj]==0) {
                if(hasCycle(adj, state, graph)) return true;
            }
        }
        state[node] = 2;
        return false;
    }
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        // Build graph
        vvi graph(numCourses, vi());
        for(int i = 0; i < prerequisites.size(); i++) {
            int a = prerequisites[i][0], b = prerequisites[i][1];
            graph[b].push_back(a);
        }
        // Detect Cycle
        vi state(numCourses, 0); // init: 0, visiting: 1, visited: 2
        for(int node = 0; node < numCourses; node++) {
            if(state[node]==0) {
                if(hasCycle(node, state, graph)) return false;
            }
        }
        return true;
    }
};

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; int numCourses; vvi prerequisites; bool ans;

    numCourses = 2; prerequisites = {{1,0}};
    ans = solution.canFinish(numCourses, prerequisites);
    assert(ans==true);

    numCourses = 2; prerequisites = {{1,0},{0,1}};
    ans = solution.canFinish(numCourses, prerequisites);
    assert(ans==false);

    numCourses = 4; prerequisites = {{0,1},{3,1},{1,3},{3,2}};
    ans = solution.canFinish(numCourses, prerequisites);
    assert(ans==false);
}