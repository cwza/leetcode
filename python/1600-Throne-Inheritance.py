from typing import List
from collections import deque

class TreeNode:
    def __init__(self, name):
        self.name = name
        self.is_dead = False
        self.successors = []
    def add_successor(self, name):
        successor = TreeNode(name)
        self.successors.append(successor)
        return successor
    def dead(self):
        self.is_dead = True
    def __repr__(self):
        return 'TreeNode({})'.format(self.name, self.is_dead)

class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king_node = TreeNode(kingName)
        self.table = {kingName: self.king_node}

    def birth(self, parentName: str, childName: str) -> None:
        parent_node = self.table[parentName]
        child_node = parent_node.add_successor(childName)
        self.table[childName] = child_node

    def death(self, name: str) -> None:
        node = self.table[name]
        node.dead()

    def getInheritanceOrder(self) -> List[str]:
        "DFS"
        result = []
        def helper(node):
            if not node.is_dead:
                result.append(node.name)
            for successor in node.successors:
                helper(successor)
        helper(self.king_node)
        # print(result)
        return result


t= ThroneInheritance("king"); # order: king
t.birth("king", "andy"); # order: king > andy
t.birth("king", "bob"); # order: king > andy > bob
t.birth("king", "catherine"); # order: king > andy > bob > catherine
t.birth("andy", "matthew"); # order: king > andy > matthew > bob > catherine
t.birth("bob", "alex"); # order: king > andy > matthew > bob > alex > catherine
t.birth("bob", "asha"); # order: king > andy > matthew > bob > alex > asha > catherine
assert t.getInheritanceOrder() == ["king", "andy", "matthew", "bob", "alex", "asha", "catherine"] # return ["king", "andy", "matthew", "bob", "alex", "asha", "catherine"]
t.death("bob"); # order: king > andy > matthew > bob > alex > asha > catherine
assert t.getInheritanceOrder() == ["king", "andy", "matthew", "alex", "asha", "catherine"] # return ["king", "andy", "matthew", "alex", "asha", "catherine"]