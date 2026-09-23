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

    def prepend(self,value):
        new = Node(value)
        if self.head is None:
            self.head = new
            self.tail = new
        else:
            self.head.prev = new
            new.next = self.head
            self.head = new

    def insert(self, value, index):
        if index>0:
            count = 0
            new = Node(value)
            current = self.head
            while current is not None:
                if count == index:
                    new.prev = current.prev
                    current.prev.next = new
                    current.prev = new
                    new.next = current


                    return True
                current = current.next
                count += 1

            return False
        else:
            print("can't use insert for index less than 1")

    def get(self,num):
        count = 0
        current = self.head
        while current is not None:
            if count == num:
                return current.data

            current = current.next
            count+=1
        return False


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
            current = self.head.next
            while current is not None:
                if current.data == value:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    return True
                current = current.next
        return None
    def display(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next
