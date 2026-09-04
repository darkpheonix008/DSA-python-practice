import node

class Queue():
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new = node.Node(value)
        if self.head is None:
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            self.tail = new

    def dequeue(self):
        if self.head is None:
            return None

        x = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return x.data

    def peek(self):
        if self.head is None:
            return None
        return self.head.data