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
            elif level > 0:
                print(" " * (level * 4) + prefixes + "Empty")

    def bubble_sort_nodes(self):
            if not self.root:
                return
        
            head = self.flatten(self.root)
            dummy = Node(0)
            dummy.right_node = head

            swapped = True
            while swapped:
                swapped = False
                previous = dummy
                actual = dummy.right_node

                while actual and actual.right_node:
                    next = actual.right_node

                    if actual.data > next.data:
                        previous.right_node = next
                        actual.right_node = next.right_node
                        next.right_node = actual
                        swapped = True
                        previous = next  
                    else:
                        previous = actual
                        actual = actual.right_node

            sorted_head = dummy.right_node

            total_nodes = self.count_of_node(sorted_head)
            self.root, _ = self.rebuild(sorted_head, total_nodes)

    # --- Métodos de bajo nivel ---
    def flatten(self, node):
        if not node:
            return None
        left = node.left_node
        right = node.right_node
        node.left_node = None
        node.right_node = None

        left_list = self.flatten(left)
        right_list = self.flatten(right)

        head = node
        tail = node
        if left_list:
            tail.right_node = left_list
            while tail.right_node:
                tail = tail.right_node
        if right_list:
            tail.right_node = right_list
        return head

    def count_of_node(self, head):
        count = 0
        while head:
            count += 1
            head = head.right_node
        return count

    def rebuild(self, head, nodes):
        if nodes <= 0 or not head:
            return None, head
        left_child, head = self.rebuild(head, nodes // 2)
        root = head
        head = head.right_node
        root.left_node = left_child
        root.right_node, head = self.rebuild(head, nodes - nodes // 2 - 1)
        return root, head

tree = Binary_tree(Node(1))
tree.root.left_node = Node(2)
tree.root.right_node = Node(3)
tree.root.left_node.left_node = Node(4)
tree.root.left_node.right_node = Node(5)
tree.root.left_node.right_node.right_node = Node(10)
print("\n=== ESTRUCTURA ORIGINAL  ===")
tree.print_structure()
tree.bubble_sort_nodes()
print("\n=== NUEVA ESTRUCTURA  ===")
tree.print_structure()

