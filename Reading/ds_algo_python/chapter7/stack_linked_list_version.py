from typing import Optional

class StackLinkedList: 
    def __init__(self):
        self._stack = None
        self._size = 0

    def __len__(self):
        return self._size

    def isEmpty(self):
        return self._size is 0

    def push(self, item: Optional[float]):
        newNode = _StackNode(item)
        newNode.next = self._stack
        self._stack = newNode
        self._size+=1

    def pop(self) -> Optional[float]:
        assert not self.isEmpty(), 'the stack is empty'
        item = self._stack._data
        self._stack = self._stack.next
        self._size -= 1
        return item

    def peek(self):
        assert not self.isEmpty(), 'the stack is empty'
        return self._stack._data

class _StackNode:
    def __init__(self, data):
        self._data = data
        self.next = None
