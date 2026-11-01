class Node:
    data: str
    left_node: "Node"
    right_node: "Node"

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left_node = left
        self.right_node = right


class Binary_tree:
    root: Node

    def __init__(self, root):
        self.root = root

    def print_structure(self, current_node= None, level=0,prefixes= "Raiz: "):
        if current_node is None and level == 0:
            current_node = self.root

        if current_node is not None:
            print(" " *(level * 4) + prefixes + str(current_node.data))
            if current_node.left_node or current_node.right_node:
                self.print_structure(current_node.left_node, level + 1,"├─ Left: " )
                self.print_structure(current_node.right_node, level + 1,"├─ Right: " )

tree = Binary_tree(Node(1))
tree.root.left_node = Node(2)
tree.root.right_node = Node(3)
tree.root.left_node.left_node = Node(4)
tree.root.left_node.right_node = Node(5)
tree.root.left_node.right_node.right_node = Node(10)
tree.print_structure()

