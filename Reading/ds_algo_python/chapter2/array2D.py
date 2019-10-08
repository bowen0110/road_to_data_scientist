from array import Array 

class Array2D:
    def __init__(self, nrows, ncols):
        self._rows = Array(nrows)
        for i in range(nrows):
            self._rows[i] = Array(ncols)


    def numRows(self):
        return len(self._rows)


    def numCols(self):
        return len(self._rows[0])


    def clear(self, value):
        for i in range(self.numRows()):
            self._rows[i].clear(value)


    def __getitem__(self, tupleIndex):
        assert len(tupleIndex) == 2, 'invalid tuple index'
        numRow, numCol = tupleIndex
        assert numRow >= 0 and numRow < self.numRows()\
                and numCol >= 0 and numCol < self.numCols(),\
                'index out of range'
        return self._rows[numRow][numCol]


    def __setitem__(self, tupleIndex, value):
        assert len(tupleIndex) == 2, 'invalid tuple index'
        numRow, numCol = tupleIndex
        assert numRow >= 0 and numRow < self.numRows()\
                and numCol >= 0 and numCol < self.numCols(),\
                'index out of range'
        self._rows[numRow][numCol] = value

