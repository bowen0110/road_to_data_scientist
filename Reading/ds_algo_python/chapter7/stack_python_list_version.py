from typing import Optional

class StackPythonList:
    def __init__(self):
        self._stack = list()


    def isEmpty(self):
        return len(self) is 0


    def __len__(self):
        return len(self._stack)

    
    def push(self, item: Optional[float]):
        self._stack.append(item)

    
    def pop(self) -> Optional[float]:
        assert not self.isEmpty(), 'the stack is empty'
        item = self._stack.pop()
        return item


    def peek(self) -> Optional[float]:
        assert not self.isEmpty(), 'the stack is empty'
        item = self._stack[-1]
        return item
