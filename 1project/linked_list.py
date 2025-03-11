"""Linked Ring List"""

from linked_list_item import LinkedListItem


class LinkedList:
    """Связный список"""

    def __init__(self, head=None):
        self.head = head
        self.tail = None

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
        else:
            ptr.next = self.head
            ptr.prev = self.tail
            self.head.prev = ptr
            self.tail.next = ptr
            self.head = ptr

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

    def append(self, item):
        """Элиас для append_right"""
        self.append_right(item)

    def remove(self, item):
        if self.head is None:
            raise ValueError("Список пуст")

        ptr = self.head
        while True:
            if ptr.data == item:
                if ptr == self.head:
                    if len(self) == 1:
                        self.head = None
                        self.tail = None
                    else:
                        self.head = self.head.next
                        self.head.prev = self.tail
                        self.tail.next = self.head
                elif ptr == self.tail:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
                else:
                    left = ptr.prev
                    right = ptr.next
                    left.next = right
                    right.prev = left
                return
            ptr = ptr.next
            if ptr == self.head:
                break
        raise ValueError("Элемент не найден")

    def insert(self, previous, item):
        """Вставка справа"""
        if previous not in self:
            raise ValueError("Не найдено значение previous")
        ptr = LinkedListItem(item)
        right = previous.next
        previous.next = ptr
        ptr.prev = previous
        right.prev = ptr
        ptr.next = right

    def __len__(self):
        count = 0
        ptr = self.head
        if ptr is None:
            return 0
        while True:
            count += 1
            ptr = ptr.next
            if ptr == self.head:
                break
        return count

    def __iter__(self):
        if not self.head:
            return
        ptr = self.head
        while True:
            yield ptr
            ptr = ptr.next
            if ptr == self.head:
                break

    def __getitem__(self, index):
        return self._get_obj(index)

    def __contains__(self, item):
        if not self.head:
            return False

        ptr = self.head
        while True:
            if ptr.data == item:
                return True
            ptr = ptr.next
            if ptr == self.head:
                return False

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

    def _get_obj(self, indx):
        if not (isinstance(indx, int)) or not (0 <= indx < len(self)):
            for i, obj in enumerate(self):
                if i == obj:
                    return obj
