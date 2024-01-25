# task1.py
class Node:
    def __init__(self, data):
        # Инициализация узла с данными и указателем на следующий узел
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        # Инициализация связного списка с начальным узлом
        self.head = None

    def push(self, val):
        # Создание нового узла
        new_node = Node(val)
        if self.head is None:
            # Если список пустой, новый узел становится головой списка
            self.head = new_node
        else:
            # Поиск последнего узла списка
            current = self.head
            while current.next:
                current = current.next
            # Добавление нового узла в конец списка
            current.next = new_node

    def get(self, index):
        # Получение узла по его индексу
        if index < 0:
            # Индекс не может быть отрицательным
            return None
        current = self.head
        for _ in range(index):
            if current is None:
                # Если достигнут конец списка до достижения нужного индекса
                return None
            current = current.next
        if current is None:
            # Если индекс выходит за пределы списка
            return None
        return current.data

    def remove(self, index):
        # Удаление узла по индексу
        if index < 0 or self.head is None:
            # Нельзя удалить узел с отрицательным индексом или из пустого списка
            return
        if index == 0:
            # Удаление первого узла списка
            self.head = self.head.next
            return
        current = self.head
        for _ in range(index - 1):
            if current is None:
                return
            current = current.next
        if current is None or current.next is None:
            return
        current.next = current.next.next

    def insert(self, n, val):
        # Вставка нового узла по индексу
        if n < 0:
            # Нельзя вставить узел с отрицательным индексом
            return
        new_node = Node(val)
        if n == 0:
            # Вставка узла в начало списка
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(n - 1):
            if current is None:
                return
            current = current.next
        if current is None:
            return
        new_node.next = current.next
        current.next = new_node

    def __iter__(self):
        # Итератор для перебора узлов списка
        current = self.head
        while current:
            yield current.data
            current = current.next

# Создание экземпляра связного списка
my_list = LinkedList()

# Добавление элементов в список
my_list.push(1)
my_list.push(2)
my_list.push(3)

# Получение элементов списка по индексу
print(my_list.get(0))  # Выводит: 1
print(my_list.get(1))  # Выводит: 2
print(my_list.get(2))  # Выводит: 3

# Удаление элемента из списка по индексу
my_list.remove(1)
print(list(my_list))  # Выводит: [1, 3]

# Вставка элемента в список по индексу
my_list.insert(1, 2)
print(list(my_list))  # Выводит: [1, 2, 3]

# Итерация по элементам списка и вывод их на экран
for item in my_list:
    print(item)
# Выводит:
# 1
# 2
# 3
