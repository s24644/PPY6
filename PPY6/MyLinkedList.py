from Element import Element


class MyLinkedList:
    def __init__(self, head=None, tail=None, size=0):
        self.head = head
        self.tail = tail
        self.size = size

    def __str__(self):
        result = ""
        current_node = self.head
        while current_node is not None:
            result += str(current_node.data) + ", "
            current_node = current_node.nextE
        return result

    def get(self, e):
        current_node = self.head
        while current_node is not None:
            if current_node.data == e.data:
                return current_node
            current_node = current_node.nextE
        return "Nie ma takiego elementu"

    def delete(self, e):
        tmp = self.head
        previous = Element.Element

        if tmp is not None:
            if tmp.data == e.data:
                self.head = tmp.nextE
                tmp = None
                return

        while tmp is not None:
            if tmp.data == e.data:
                break
            previous = tmp
            tmp = tmp.nextE

        if tmp is None:
            return

        previous.nextE = tmp.nextE

        tmp = None

    def append(self, e, func=None):
        new_element = Element(e)
        new_element.nextE = self.head
        self.head = new_element




