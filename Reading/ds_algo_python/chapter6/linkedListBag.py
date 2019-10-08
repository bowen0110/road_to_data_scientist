class LinkedListBag:
    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def add(self, value):
        newNode = _BagNode(value)
        newNode._next = self._head
        self._head = newNode
        self._size += 1

    def remove(self, value):
        preNode = None
        curNode = self._head

        while curNode is not None and curNode._data != value:
            preNode = curNode
            curNode = curNode._next

        assert curNode is not None, 'no such element in Bag'
        if curNode is self._head:
            self._head = curNode._next
        else:
            preNode._next = curNode._next
            curNode._next = None
        self._size -= 1
    
    def search(self, value):
        curNode = self._head
        while curNode is not None and curNode._data != value:
            curNode = curNode._next
        return curNode is not None

    def __iter__(self):
        return _LinkedListBagIterator(self._head)


class _LinkedListBagIterator:
    def __init__(self, listHead):
        self._curNode = listHead

    def __iter__(self):
        return self

    def __next__(self):
        if self._curNode is not None:
            item = self._curNode
            self._curNode = self._curNode._next
            return item
        else:
            raise StopIteration


class _BagNode:
    def __init__(self, value):
        self._data = value
        self._next = None