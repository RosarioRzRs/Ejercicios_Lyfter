class Node:
    data: str
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        

class Stack:
    head: Node

    def __init__(self, head):
        self.head = head

    def print_structure(self):
        current_node = self.head
        print("****")
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def push(self, new_node):
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head:
          self.head = self.head.next


first_node = Node("3")
my_stack = Stack(first_node)
my_stack.print_structure()

second_node = Node("8")
my_stack.push(second_node)
my_stack.print_structure()

third_node = Node("5")
my_stack.push(third_node)
my_stack.print_structure()

my_stack.pop()
my_stack.print_structure()
my_stack.pop()
my_stack.print_structure()
my_stack.pop()
my_stack.print_structure()
my_stack.pop()
my_stack.print_structure()

