#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;

class Solution {
// Topological Sort by reversed dfs end time, Time: O(V+E), Space: O(V)
public:
    bool dfs(int node, vector<int> &state, vi &ans, vvi &graph) {
        // If has cycle return true
        state[node] = 1;
        for(int adj : graph[node]) {
            if(state[adj] == 1) return true;
            if(state[adj] == 0) {
                if(dfs(adj, state, ans, graph)) return true;
            }
        }
        state[node] = 2;
        ans.push_back(node);
        return false;
    }
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        // Build graph
        vvi graph(numCourses, vi());
        for(int i = 0; i < prerequisites.size(); i++) {
            int a = prerequisites[i][0], b = prerequisites[i][1];
            graph[b].push_back(a);
        }

        // Topological Sort
        vi ans; 
        vector<int> state(numCourses, 0); // init: 0, visiting: 1, visited: 2
        for(int node = 0; node < numCourses; node++) {
            if(state[node]==0) {
                if(dfs(node, state, ans, graph)) return vi(); // if has cycle return []
            }
        }
        reverse(ans.begin(), ans.end());
        return ans;
    }
};

void printAns(vi ans) {
    for(int node : ans) cout << node << " ";
    cout << endl;
}

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    Solution solution; int numCourses; vvi prerequisites; vi ans;

    numCourses = 2; prerequisites = {{1,0}};
    ans = solution.findOrder(numCourses, prerequisites);
    printAns(ans); // [0, 1]

    numCourses = 4; prerequisites = {{1,0},{2,0},{3,1},{3,2}};
    ans = solution.findOrder(numCourses, prerequisites);
    printAns(ans); // [0,2,1,3]

    numCourses = 1; prerequisites = {};
    ans = solution.findOrder(numCourses, prerequisites);
    printAns(ans); // [0]

    numCourses = 2; prerequisites = {{0,1},{1,0}};
    ans = solution.findOrder(numCourses, prerequisites);
    assert(ans==vi()); // []
}