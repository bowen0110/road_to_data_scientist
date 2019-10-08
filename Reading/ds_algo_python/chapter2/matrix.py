from array2D import Array2D

class Matrix:
    def __init__( self, rows, cols ):
        self._matrix = Array2D(rows, cols)
        self._matrix.clear(0)


    def numRows( self ):
        return self._matrix.numRows()


    def numCols( self ):
        return self._matrix.numCols()


    def __getitem__( self, indexTuple ):
        return self._matrix[ indexTuple[0], indexTuple[1] ]


    def __setitem__( self, indexTuple, scalar ):
        self._matrix[ indexTuple[0], indexTuple[1] ] = scalar


    def scaleBy( self, scalar ):
        for row in range( self.numRows() ):
            for col in range( self.numCols() ):
                self[row, col] *= scalar


    def transpose( self ):
        tempMatrix = Matrix( self.numCols(), self.numRows() )
        for row in range( self.numCols() ):
            for col in range( self.numRows() ):
                tempMatrix[row, col] = self[col, row]
        return tempMatrix


    def __add__( self, rhsMatrix ):
        assert self.numRows() == rhsMatrix.numRows() and\
                self.numCols() == rhsMatrix.numCols(), \
                'invalid rhsMatrix'
        sumMatrix = Matrix( self.numRows(), self.numCols() )
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                sumMatrix[i, j] = self[i, j] + rhsMatrix[i, j]
        return sumMatrix


    def __sub__( self, rhsMatrix ):
        assert self.numRows() == rhsMatrix.numRows() and \
                self.numCols() == rhsMatrix.numCols(), \
                'invalid rhsMatrix'
        subMatrix = Matrix( self.numRows(), self.numCols() )
        for i in range( self.numRows() ):
            for j in range( self.numCols() ):
                subMatrix[i, j] = self[i, j] - rhsMatrix[i, j]
        return subMatrix


    def __mul__( self, rhsMatrix ):
        assert self.numCols() == rhsMatrix.numRows(), 'Invalid rhsMatrix'
        mulMatrix = Matrix(self.numRows(), rhsMatrix.numCols())
        for i in range(mulMatrix.numRows()):
            for j in range(mulMatrix.numCols()):
                for n in range(self.numCols()):
                    mulMatrix[i, j] += self[i, n]*rhsMatrix[n, j]
        return mulMatrix