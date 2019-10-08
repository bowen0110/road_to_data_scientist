from array import Array 

class MultiArray:
    def __init__( self, *dimensions ):
        assert len( dimensions ) > 1, 'invalid dimensions, must be greater than 1'
        self._dimensions = dimensions

        # get total number of elements in the Array
        totalElements = 1
        for dimLength in dimensions:
            assert dimLength > 0, 'each dimension must have at least 1 element'
            totalElements *= dimLength
        self._multiArray = Array( totalElements )
        self.clear( None )

        # set factors to be a array
        self._factors = Array( len( dimensions ) )
        self._computeFactors()

    def numDims( self ) -> int:
        return len( self._dimensions )

    def length( self, dimNum ) -> int:
        assert 1 <= dimNum and dimNum < len( self._dimensions ), 'inputed dimension out of range'
        return self._dimensions[ dimNum - 1 ]

    def clear( self, value ):
        self._multiArray.clear( value )

    def __getitem__( self, nTuple ) -> 'Value':
        assert len( nTuple ) is self.numDims(), 'Invalid index'
        nDex = self._computeIndex( nTuple )
        assert nDex is not None, 'index out of range'
        return self._multiArray[ nDex ]


    def __setitem__( self, nTuple, value ):
        assert len( nTuple ) is self.numDims(), 'Invalid index'
        nDex = self._computeIndex( nTuple )
        assert nDex is not None, 'index out of range'
        self._multiArray[ nDex ] = value


    def _computeIndex( self, nTuple ):
        result = 0
        for i in range( len( nTuple )):
            if nTuple[i] < 0 or nTuple[i] >= self.length( i ):
                return None
            else:
                result += nTuple[i] * self._factors[ i ]
        return result

    def _computeFactors( self ):
        for i in range( self.numDims() ):
            count = i+1
            f = 1
            while count < self.numDims():
                f *= self._dimensions[count]
                count += 1
            self._factors[i] = f




