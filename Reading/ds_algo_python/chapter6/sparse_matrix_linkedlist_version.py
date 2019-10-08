from array_linear import Array
from typing import Optional, List

class SparseMatrixLinkedList:
    def __init__(self, rows: int, cols: int):
        self._numCols = cols
        self._matrix = Array(rows)

    
    def numRows(self):
        return len(self._matrix)


    def numCols(self):
        return self._numCols


    def __getitem__(self, nTuple: List[int]) -> float:
        row, col = nTuple[0], nTuple[1]
        assert 0<=row and row<self.numRows(), 'index out of range'
        assert 0<=col and col<self.numCols(), 'index out of range'
        curNode = self._matrix[row]

        while curNode is not None and curNode._col is not col:
            curNode = curNode._next

        if curNode is None:
            return 0.0
        else:
            return curNode._data
        

    def __setitem__(self, nTuple: List[int], value: Optional[float]):
        row, col = nTuple[0], nTuple[1]
        assert 0<=row and row<self.numRows(), 'index out of range'
        assert 0<=col and col<self.numCols(), 'index out of range'
        preNode = None
        curNode = self._matrix[row]

        while curNode is not None and curNode._col < col:
            preNode = curNode
            curNode = curNode._next

        # already have element at the position
        if curNode is not None and curNode._col is col:
            if value is 0.0:
                if curNode is self._matrix[row]:
                    self._matrix[row] = None
                else:
                    preNode.next = curNode.next
            else:
                curNode._data = value
        # no element at this position
        else:
            if value is not 0.0:
                newNode = _SparseMatrixNode(col, value)
                if curNode is self._matrix[row]:
                    self._matrix[row] = newNode
                else:
                    preNode.next = newNode
                    newNode.next = curNode


    def scaleBy(self, scalar: float):
        for row in self._matrix:
            curNode = row
            while curNode is not None:
                curNode._data *= scalar
                curNode = curNode._next

    
    def transpose(self):
        pass


    def __add__(self, rhsMatrix):
        pass


    def __sub__(self, rhsMatrix):
        pass

    def __mul__(self, rhsMatrix):
        pass


            


class _SparseMatrixNode:
    def __init__(self, col: int, data: Optional[float]):
        self._data = data
        self._col = col
        self._next = None

