class Arrays:
    def __init__(self,):
        self.list1 = []

    def display(self):
        index = 0
        while index != len(self.list1):
            current = self.list1[index]
            print(current)
            index += 1

    def search(self, value):
        if len(self.list1)>0:
            index = 0
            while index != len(self.list1):
                current = self.list1[index]
                if current == value:
                    return index
                index += 1
            return -1
        return None

    def bubble_sort(self):
        if len(self.list1)>1:
            for i in range (len(self.list1)):
                for j in range (1,len(self.list1)-i):
                    if self.list1[j-1]>self.list1[j]:
                        self.list1[j-1], self.list1[j] = self.list1[j], self.list1[j-1]
            return True
        elif len(self.list1)== 1:
            return True

        return None

    def selection_sort(self):
        if len(self.list1)>1:
            for i in range (len(self.list1)):
                small = i
                for j in range (i+1,len(self.list1)):
                    if self.list1[j]< self.list1[small]:
                        small = j
                self.list1[i], self.list1[small] = self.list1[small], self.list1[i]

            return True
        elif len(self.list1) == 1:
            return True

        return None

    def insertion_sort(self):
            if len(self.list1) > 1:
                for i in range(1, len(self.list1)):
                    current = self.list1[i]
                    j = i - 1

                    while j >= 0 and self.list1[j] > current:
                        self.list1[j + 1] = self.list1[j]
                        j -= 1

                    self.list1[j + 1] = current

                return True

            elif len(self.list1) == 1:
                return True

            return None

