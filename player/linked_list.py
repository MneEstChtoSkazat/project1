class LinkedListItem:
    """Узел связного списка"""

    def __init__(self, data, prev=None, next=None):
        self.__data = data
        self.__prev = prev
        self.__next = next

    @property
    def next_item(self):
        """Следующий элемент"""
        return self.__next

    @next_item.setter
    def next_item(self, value):
        self.__next = value

    @property
    def previous_item(self):
        """Предыдущий элемент"""
        return self.__prev

    @previous_item.setter
    def previous_item(self, value):
        self.__prev = value

    def __repr__(self):
        return f"{self}"


class LinkedList:
    """Связный список"""

    def __init__(self, first_item=None, tail=None, ptr=None):
        self.first_item = self.tail = self.ptr = None
        self.count = 0
        self.left = None
        self.right = None

    @property
    def last(self):
        """Последний элемент"""
        raise NotImplementedError()

    def append_left(self, item):
        """Добавление слева"""
        raise NotImplementedError()

    def append_right(self, item):
        """Добавление справа"""
        if self.first_item is None:
            self.first_item = item
            self.tail = item
            self.count += 1
        else:
            self.ptr = item
            self.tail.next_item = self.ptr
            self.ptr.previous_item = self.tail
            self.tail = self.ptr
            self.count += 1

    def append(self, item):
        """Добавление справа"""
        raise NotImplementedError()

    def remove(self, item):
        """Удаление"""
        raise NotImplementedError()

    def insert(self, previous, item):
        """Вставка справа"""
        raise NotImplementedError()

    def __len__(self):
        return self.count

    def __iter__(self):
        raise NotImplementedError()

    def __getitem__(self, index):
        raise NotImplementedError()

    def __contains__(self, item):
        raise NotImplementedError()

    def __reversed__(self):
        raise NotImplementedError()
