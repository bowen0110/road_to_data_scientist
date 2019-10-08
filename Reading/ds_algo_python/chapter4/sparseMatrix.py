class SparseMatrix:
    def __init__( self, rows, cols ):
        self._numRows = rows
        self._numCols = cols
        self._entryList = list()
    
    def numRows( self ):
        return self._numRows

    def numCols( self ):
        return self._numCols

    def __contains__( self, value ):
        for i in range( len(self._entryList) ):
            if self._entryList[i]._value == value:
                return True
        return False

    def __setitem__( self, aTuple, value ):
        assert 0 <= aTuple[0] and aTuple[0] < self._numRows, 'Invalid index'
        assert 0 <= aTuple[1] and aTuple[1] < self._numCols, 'Invalid index'
        nDx = self._findPosition( aTuple[0], aTuple[1] )
        if nDx is None:
            if value != 0.0:
                newEntry = MatrixEntry( value, aTuple )
                self._entryList.append( newEntry )
        else:
            if value != 0.0:
                self._entryList[nDx]._value = value
            else:
                self._entryList.pop( nDx )
        
    def __getitem__( self, aTuple ):
        assert 0 <= aTuple[0] and aTuple[0] < self._numRows, 'Invalid index'
        assert 0 <= aTuple[1] and aTuple[1] < self._numCols, 'Invalid index'
        nDx = self._findPosition( aTuple[0], aTuple[1] )
        if nDx is None:
            return 0
        else:
            return self._entryList[nDx]._value

    def scaleBy( self, scalar ):
        for i in range( len(self._entryList) ):
            self._entryList[i]._value *= scalar
    
    def __add__( self, rhsMatrix ) -> 'added matrix':
        assert self._numRows == rhsMatrix.numRows() and \
             self._numCols == rhsMatrix.numCols(), \
                 'must be equal size matrix'

        newMatrix = SparseMatrix( self._numRows, self._numCols )
        for entry in self._entryList:
            newEntry = MatrixEntry( entry._value, (entry._row, entry._col) )
            newMatrix._entryList.append( newEntry )
        
        for entry in rhsMatrix._entryList:
            value = newMatrix[entry._row, entry._col]
            value += entry._value
            newMatrix[entry._row, entry._col] = value
        
        return newMatrix

    def __sub__( self, rhsMatrix ):
        assert rhsMatrix.numRows() == self._numRows and\
            rhsMatrix.numCols() == self._numCols, \
                'matrix dont have the same size'  # O(1)
        
        newMatrix = SparseMatrix( self._numRows, self._numCols ) # O(1)
        
        # k entry in the list
        # for statement runs k times
        for entry in self._entryList: 
            newEntry = MatrixEntry( entry._value, (entry._row, entry._col) ) # O(1)
            newMatrix._entryList.append( newEntry ) # append() amortized cost O(1)
        # above for loop runs O(k)
        
        # k entry in the list
        # for loop runs k times
        for entry in rhsMatrix._entryList:
            value = newMatrix[entry._row, entry._col] # O(k)
            value -= entry._value # O(1)
            newMatrix[entry._row, entry._col] = value # O(k)
        # above for loop runs O(k^2)
        
        return newMatrix
        # the function __sub__ has O(k^2) running time


    def _findPosition( self, row, col ):
        for i in range( len(self._entryList) ):
            if self._entryList[i]._row == row and self._entryList[i]._col == col:
                return i
        return None


    



class MatrixEntry:
    def __init__( self, value, aTuple ):
        self._value = value
        self._row = aTuple[0]
        self._col = aTuple[1]