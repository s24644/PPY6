from Element import Element


class MyLinkedList:
    def __init__(self, head=None, tail=None, size=0):
        self.head = head
        self.tail = tail
        self.size = size

    def __str__(self):
        result = ""
        current = self.head
        while current:
            result = result + str(current.data) + ', '
            current = current.nextE
        return result[0:len(result)-2]

    def get(self, e):
        if self.head.data == e:
            self.head = self.head.nextE
            return

        current = self.head
        while current:
            if current.data == e:
                break
            current = current.nextE

        if current is None:
            print("Nie znaleziono podanej wartości")
            return
        else:
            return current.data

    def delete(self, e):
        if self.head.data == e:
            self.head = self.head.nextE
            return

        current = self.head
        while current:
            if current.data == e:
                break
            previous = current
            current = current.nextE

        if current is None:
            print("Nie znaleziono podanej wartości")
        else:
            previous.nextE = current.nextE

    def append(self, e, func=None):
        new_element = Element(e)

        if self.head is None:
            self.head = new_element

        if func is None:
            if self.head.data >= new_element.data:
                new_element.nextE = self.head
                self.head = new_element

            else:
                current = self.head
                while current.nextE and new_element.data > current.nextE.data:
                    current = current.nextE

                new_element.nextE = current.nextE
                current.nextE = new_element
        else:
            if func(self.head.data, new_element.data):
                new_element.nextE = self.head
                self.head = new_element

            else:
                current = self.head
                while current.nextE and new_element.data > current.nextE.data:
                    current = current.nextE

                new_element.nextE = current.nextE
                current.nextE = new_element




