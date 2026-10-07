class Node:
    data: int
    next: "Node"
    previous: "Node"

    def __init__(self, data, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous

        

class LinkedList:
    front: Node
    back: Node

    def __init__(self, front=None, back=None):
        self.front = front
        self.back = back

    def print_all(self):
        current_node = self.front
        message = ""
        if current_node is None:
            message = "Ningun nodo"
        while current_node is not None:
            message += str(current_node.data)
            if current_node.next is not None:
                message += " -> "
            current_node = current_node.next

        
        print(message)

    def insert_front(self, data):
        new_node = Node(data)
        if self.front is None:
            self.front = new_node
            self.back = new_node
        else:
            new_node.next = self.front
            self.front.previous = new_node
            self.front = new_node
            

    def insert_back(self, data):
        new_node = Node(data)
        if self.back is None:
            self.front = new_node
            self.back = new_node
        else:
            new_node.previous = self.back
            self.back.next = new_node
            self.back = new_node


    def delete(self, data):
        current_node = self.front
        if current_node.data == data:
            self.front = current_node.next
            if self.front is not None:
                self.front.previous = None
        else:
            previous_node= current_node
            current_node = current_node.next
            while current_node is not None:
                if current_node.data == data:
                    previous_node.next = current_node.next
                    if current_node.next is not None:
                        current_node.next.previous = previous_node
                    else:
                        self.back = previous_node
                    break
                else:  
                    previous_node= current_node                  
                    current_node = current_node.next


q = LinkedList()

q.insert_front(10)
q.insert_front(20)
q.insert_back(30)
q.insert_back(35)
q.insert_front(5)
q.insert_back(88)
q.insert_back(3)


q.print_all()

q.delete(88)
q.print_all()

q.delete(3)
q.print_all()

q.insert_back(100)
q.print_all()

q.delete(10)
q.print_all()


q.delete(100)
q.delete(35)
q.delete(5)
q.delete(30)
q.print_all()

q.delete(20)
q.print_all()

