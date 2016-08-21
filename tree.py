from __future__ import print_function
from collections import deque

class Node():
    def __init__(self, data, parent=None):
        self.children = []
        self.parent = parent
        self.data = data

    def add(self, node):
        node.parent = self
        self.children.append(node)

class Tree():
    def __init__(self, root_node):
        self.root = root_node

    def traverseDF(self, cb, node=None):
        curr = node if node else self.root

        cb(curr)

        for child in curr.children:
            self.traverseDF(cb, child)

    def traverseBF(self, cb, node=None):
        curr = node if node else self.root
        q = deque()

        q.append(curr)

        while len(q) > 0:
            curr = q.popleft()
            cb(curr)

            for child in curr.children:
                q.append(child)

    def contains(self, search_data, traversal=None):
        # traverse to find the specific node and add the given node as a child
        traverse = traversal if traversal else self.traverseDF

        def find_node(n):
            if n.data == search_data:
                find_node.found = n

        """use a function attribute to avoid local/nonlocal issues when performing
        assignment within a closure
        In Python3 the nonlocal keyword could be used
        """
        find_node.found = None

        traverse(find_node)

        return find_node.found


    def add(self, new_child, to_parent_data, traversal=None):
        # if given a node, use it as the child, if given data instantiate a new node
        new_child = new_child if isinstance(new_child, Node) else Node(new_child)

        parent = self.contains(to_parent_data)

        if parent:
            parent.add(new_child)

            return True

    def find_depth(self, node):
        # if given a node, use that, otherwise find the node that contains the given data
        node = node if isinstance(node, Node) else tree.contains(node)
        depth = 0

        while node.parent is not None:
            depth += 1
            node = node.parent

        return depth

    def print(self):
        def print_with_format(n):
            line = ""
            depth = self.find_depth(n)


            if depth > 0:
                if depth > 1:
                    line += "|"
                    line += " " * (depth - 2)

                line += "  " * (depth - 1)
                line += "|--"

            line += n.data

            print(line)

        self.traverseDF(print_with_format)


tree = Tree(Node("CEO"))

tree.add("COO", "CEO")
tree.add("CFO", "CEO")
tree.add("CTO", "CEO")
tree.add("VP of Engineering", "CTO")
tree.add("Director of Engineering", "VP of Engineering")
tree.add("Lead Engineer", "Director of Engineering")
tree.add("Eng 1", "Lead Engineer")
tree.add("Eng 2", "Lead Engineer")
tree.add("VP of Finance", "CFO")
tree.add("Accountant", "VP of Finance")

print_data = lambda x: print(x.data)
tree.print()
# tree.traverseBF(print_data)
