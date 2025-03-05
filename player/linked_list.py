from linked_list_item import LinkedListItem


class LinkedList:
    """Связный список"""

    def __init__(self):
        self.head = self.tail = None
        self.count = 0

    @property
    def last(self):
        """Последний элемент"""
        if len(self) == 0:
            return None
        return self.tail

    def append_left(self, item):
        """Добавление элемента в начало списка"""
        ptr = LinkedListItem(item)
        if len(self) == 0:
            self.head = ptr
            self.tail = ptr
            self.head.next = self.head
            self.head.prev = self.head
            return
        else:
            ptr.next = self.head
            ptr.prev = self.tail
            self.head.prev = ptr
            self.tail.next = ptr
            self.head = ptr
        self.count += 1

    def append_right(self, item):
        """Добавление элемента в конец списка"""
        ptr = LinkedListItem(item)
        if len(self) == 0:
            self.head = ptr
            self.tail = ptr
            self.head.next = self.head
            self.head.prev = self.head
        else:
            self.tail.next = ptr
            ptr.prev = self.tail
            self.tail = ptr
            self.tail.next = self.head
            self.head.prev = self.tail
        self.count += 1

    def append(self, item):
        """Добавление справа"""
        raise NotImplementedError()

    def remove(self, item):
        """Удаление"""
        if self.count == 0:
            raise ValueError("Список пуст")
        ptr = self.head
        while True:
            if ptr.data == item:
                if ptr == self.head:
                    ptr = self.head.next
                    ptr.prev = self.tail
                    self.tail.next = ptr
                    self.head = ptr
                elif ptr == self.tail:
                    ptr = self.tail.prev
                    ptr.next = self.head
                    self.tail = ptr
                else:
                    left = ptr.prev
                    right = ptr.next
                    left.next = right
                    right.prev = left
                self.count -= 1
                return
            ptr = ptr.next
        raise ValueError("Элемент не найден")

    def insert(self, previous, item):
        """Вставка справа"""
        ptr = LinkedListItem(item)
        right = previous.next
        previous.next = ptr
        ptr.prev = previous
        right.prev = ptr
        ptr.next = right

    def __len__(self):
        return self.count

    def __iter__(self):
        raise NotImplementedError()

    def __getitem__(self, index):
        raise NotImplementedError()

    def __contains__(self, item):
        raise NotImplementedError()

    def __reversed__(self):
        if len(self) == 0:
            return []
        reversed_list = []
        last = self.tail
        while True:
            reversed_list.append(last.data)
            if last == self.head:
                break
            last = last.prev
        return reversed_list
