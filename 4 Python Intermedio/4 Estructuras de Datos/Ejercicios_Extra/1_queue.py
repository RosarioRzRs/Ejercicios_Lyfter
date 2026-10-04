class Node:
    data: str
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Queue:
    head: Node

    def __init__(self, head=None):
        self.head = head

    def print_all(self):
        current_node = self.head
        message = ""
        while current_node is not None:
            message += current_node.data
            if current_node.next is not None:
                message += "-> "
            current_node = current_node.next
        print(message)

    def enqueue(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head

            while current_node.next is not None:
                current_node = current_node.next

            current_node.next = new_node

    def dequeue(self):
        if self.head:
          deleted_node = f"Nodo eliminado: {self.head.data}"
          print(deleted_node)
          self.head = self.head.next


q = Queue()

q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.print_all()

q.dequeue()
q.print_all()

