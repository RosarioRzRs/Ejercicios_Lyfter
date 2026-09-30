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

first_node = Node("3")
my_double_ended_queue = Double_ended_queue(first_node)
my_double_ended_queue.print_structure()

print("**** PUSH*****")
second_node = Node("8")
my_double_ended_queue.push_left(second_node)
my_double_ended_queue.print_structure()

third_node = Node("5")
my_double_ended_queue.push_right(third_node)
my_double_ended_queue.print_structure()

fourth_node = Node("9")
my_double_ended_queue.push_right(fourth_node)
my_double_ended_queue.print_structure()

fifth_node = Node("7")
my_double_ended_queue.push_left(fifth_node)
my_double_ended_queue.print_structure()

print("**** POP*****")
my_double_ended_queue.pop_left()
my_double_ended_queue.print_structure()

my_double_ended_queue.pop_left()
my_double_ended_queue.print_structure()

my_double_ended_queue.pop_right()
my_double_ended_queue.print_structure()

my_double_ended_queue.pop_right()
my_double_ended_queue.print_structure()

my_double_ended_queue.pop_right()
my_double_ended_queue.print_structure()

my_double_ended_queue.pop_right()
my_double_ended_queue.print_structure()

my_double_ended_queue.pop_left()
my_double_ended_queue.print_structure()