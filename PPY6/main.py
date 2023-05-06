from MyLinkedList import MyLinkedList
from Element import Element

list = MyLinkedList()
list.head = Element(3)
list.append(6)
list.append(4)
list.append(3)
print("=========WEJŚCIOWA LISTA==========")
print(list)
print("=========ZWRÓCENIE ELEMENTU=========")
print(list.get(4))
list.delete(4)
print("=========PO USUNIĘCIU ELEMENTU=========")
print(list)

