class Node:
    data: str
    next: "Node"
    previous: "Node"

    def __init__(self, data, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous

        

class Double_LinkedList:
    front: Node
    back: Node

    def __init__(self, front=None, back=None):
        self.front = front
        self.back = back

    def print_forward(self):
        current_node = self.front
        message = ""
        if current_node is None:
            message = "Ningun nodo"
        while current_node is not None:
            message += current_node.data
            if current_node.next is not None:
                message += " -> "
            current_node = current_node.next
        print(message)


    def print_backward(self):
        current_node = self.back
        message = ""
        if current_node is None:
            message = "Ningun nodo"
        while current_node is not None:
            message += current_node.data
            if current_node.previous is not None:
                message += " -> "
            current_node = current_node.previous
        print(message)

    def prepend(self, data):
        new_node = Node(data)
        if self.front is None:
            self.front = new_node
            self.back = new_node
        else:
            new_node.next = self.front
            self.front.previous = new_node
            self.front = new_node
            

    def append(self, data):
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
            if self.front is None:
                self.back = current_node.next
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


dll = Double_LinkedList()
dll.append("A")
dll.append("B")
dll.append("C")
dll.print_forward()
dll.print_backward()

dll.prepend("X")
dll.print_forward()
dll.print_backward()

dll.delete("B")
dll.print_forward()
dll.print_backward()

dll.delete("C")
dll.print_forward()
dll.print_backward()

dll.delete("A")
dll.print_forward()
dll.print_backward()

dll.delete("X")
dll.print_forward()
dll.print_backward()
