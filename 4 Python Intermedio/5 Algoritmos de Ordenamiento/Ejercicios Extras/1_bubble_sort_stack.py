class Node:
    data: int
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

    def __len__(self):
        current_node = self.head
        count = 0
        while current_node is not None:
            count += 1
            current_node = current_node.next

        return count
       

    def bubble_sort(self):
        length_of_structure = len(self)-1
        for index_main in range (length_of_structure):
            current_node = self.head
            swap = False
            for index in range (length_of_structure - index_main ):
                if current_node.next.data < current_node.data:
                    print(f"Se intercambia {current_node.next.data} por {current_node.data}")
                    node_to_move = current_node.next
                    current_node.next = current_node.next.next
                    node_to_move.next = current_node
                    if index == 0:
                        self.head = node_to_move
                    else:
                        previous_node.next = node_to_move
                    current_node = node_to_move
                    swap = True
                else:
                    print(f"Sin cambios, {current_node.data} y {current_node.next.data}  se quedan igual")
                    
                previous_node = current_node
                current_node = current_node.next
                
            if not swap:
                break
        


first_node = Node(5)
my_stack = Stack(first_node)
my_stack.print_structure()

second_node = Node(9)
my_stack.push(second_node)
my_stack.print_structure()

third_node = Node(3)
my_stack.push(third_node)
my_stack.print_structure()



four_node = Node(7)
my_stack.push(four_node)
my_stack.print_structure()

five_node = Node(8)
my_stack.push(five_node)
my_stack.print_structure()

# my_stack.pop()
# my_stack.print_structure()
# my_stack.pop()
# my_stack.print_structure()
# my_stack.pop()
# my_stack.print_structure()
# my_stack.pop()
# my_stack.print_structure()


my_stack.bubble_sort()
my_stack.print_structure()

# four_node = Node(100)
# my_stack.push(four_node)
# my_stack.print_structure()

# my_stack.bubble_sort()
# my_stack.print_structure()