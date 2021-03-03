from typing import List
from collections import defaultdict

'''
Think this as a graph problem.
'''

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def gen_graph(equations, values):
            ''' equations: [["a","b"],["b","c"]], values = [2.0,3.0]
                graph: {'a': [('b', 2.0)], 'b': [('a', 0.5), ('c', 3.0)], 'c': [('b', 0.3333333333333333)]}
            '''
            graph = defaultdict(lambda : [])
            for (start, end), value in zip(equations, values):
                graph[start].append((end, value))
                graph[end].append((start, 1.0/value))
            return graph

        def get_result(graph, start, end):
            "Run dfs to find path from start to end"
            # if start in graph and start == end: return 1
            if start not in graph or end not in graph: return -1
            def dfs(node, visited):
                if node == end: return 1
                for child, value in graph[node]:
                    if child in visited: continue
                    visited[node] = True
                    result = dfs(child, visited)
                    visited[node] = False
                    if result != -1:
                        return result * value
                return -1
            return dfs(start, {start: True})

        graph = gen_graph(equations, values)
        return [get_result(graph, query[0], query[1]) for query in queries]

equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
result = Solution().calcEquation(equations, values, queries)
assert result == [6.0, 0.5, -1.0, 1.0, -1.0 ]

equations = [["a","b"],["b","c"],["bc","cd"]]
values = [1.5,2.5,5.0]
queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
result = Solution().calcEquation(equations, values, queries)
assert result == [3.75000,0.40000,5.00000,0.20000]

equations = [["a","b"]]
values = [0.5]
queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
result = Solution().calcEquation(equations, values, queries)
assert result ==  [0.50000,2.00000,-1.00000,-1.00000]