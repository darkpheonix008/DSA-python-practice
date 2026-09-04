import node

class Stack():
    def __init__(self):
        self.head = None

    def push(self, value):
        new = node.Node(value)
        new.next = self.head
        self.head = new

    def pop(self):
        x = self.head
        if self.head is None:
            return False
        elif self.head.next is not None:
            self.head = self.head.next
        else:
            self.head = None

        return x.data

    def peek(self):
        if self.head is not None:
            return self.head.data
        else:
            return None