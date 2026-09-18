class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def append(self,value):
        new = Node(value)
        if self.head is None:
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            new.prev = self.tail
            self.tail = new


    def delete(self,value):
        if self.head is None:
            return False
        if self.head.data == value:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
                return True
            else:
                self.head.prev = None
                return True
        elif self.tail.data == value:
            self.tail = self.tail.prev
            if self.tail is None:
                self.head = None
                return True
            else:
                self.tail.next = None
                return True
        else:
            current = self.head
            if current.data == value:
                current.prev.next = current.next
                current.next.prev = current.prev
        return None


