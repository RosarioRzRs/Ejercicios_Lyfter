class Node:
    data: str
    next: "Node"
    previous: "Node"

    def __init__(self, data, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous

        

class Double_ended_queue:
    head: Node
    tail: Node

    def __init__(self, head):
        self.head = head
        self.tail = head

    def print_structure(self):
        current_node = self.head
        print("****")
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def push_left(self, new_node):
        new_node.next = self.head
        self.head.previous = new_node
        self.head = new_node

    def push_right(self, new_node):
        self.tail.next = new_node
        new_node.previous = self.tail
        self.tail = new_node


    def pop_left(self):
        if self.head:
            self.head = self.head.next
            if self.head is not None:
                self.head.previous = None
            else:
                self.tail = None

    def pop_right(self):
        if self.tail:
            self.tail = self.tail.previous
            if self.tail is not None:
                self.tail.next = None
            else:
                self.head = None


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
                    if index is not length_of_structure - 1:
                        current_node.next.next.previous = current_node
                    if index != 0:
                        current_node.previous.next = node_to_move
                    current_node.next = current_node.next.next
                    node_to_move.next = current_node
                    if index == 0:
                        node_to_move.previous = None
                        self.head = node_to_move 
                    else:
                        node_to_move.previous = current_node.previous
                    current_node.previous = node_to_move
                    if index == length_of_structure - 1:
                        self.tail = current_node
                    node_to_move.next = current_node
                    current_node = node_to_move
                    swap = True
                else:
                    print(f"Sin cambios, {current_node.data} y {current_node.next.data}  se quedan igual")
                self.print_structure()
                current_node = current_node.next
                
            if not swap:
                break

first_node = Node("3")
my_double_ended_queue = Double_ended_queue(first_node)
my_double_ended_queue.print_structure()

print("**** PUSH*****")
second_node = Node("7")
my_double_ended_queue.push_left(second_node)
my_double_ended_queue.print_structure()

third_node = Node("9")
my_double_ended_queue.push_right(third_node)
my_double_ended_queue.print_structure()

fourth_node = Node("5")
my_double_ended_queue.push_right(fourth_node)
my_double_ended_queue.print_structure()

fifth_node = Node("8")
my_double_ended_queue.push_left(fifth_node)
my_double_ended_queue.print_structure()

my_double_ended_queue.bubble_sort()
my_double_ended_queue.print_structure()

# print("**** POP*****")
# my_double_ended_queue.pop_left()
# my_double_ended_queue.print_structure()

# my_double_ended_queue.pop_left()
# my_double_ended_queue.print_structure()

# my_double_ended_queue.pop_right()
# my_double_ended_queue.print_structure()

# my_double_ended_queue.pop_right()
# my_double_ended_queue.print_structure()

# my_double_ended_queue.pop_right()
# my_double_ended_queue.print_structure()

# my_double_ended_queue.pop_right()
# my_double_ended_queue.print_structure()

# my_double_ended_queue.pop_left()
# my_double_ended_queue.print_structure()