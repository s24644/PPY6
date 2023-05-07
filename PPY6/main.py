from MyLinkedList import MyLinkedList
from Element import Element
from Student import Student

my_list = MyLinkedList()
my_list.head = Element(3)
my_list.append(6)
my_list.append(4)
my_list.append(3)
print("=========WEJŚCIOWA LISTA==========")
print(my_list)
print("=========ZWRÓCENIE ELEMENTU=========")
print(my_list.get(4))
my_list.delete(4)
print("=========PO USUNIĘCIU ELEMENTU=========")
print(my_list)

print("=========ZADANIE 2============")

grades = [40, 20, 20, 20, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
student = Student("ggg", "jan", "kowalski", grades, -1, "status")
print("student przed ocena ", student)
student.assign_grade()
print("student po ocenie ", student)

