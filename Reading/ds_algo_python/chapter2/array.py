import ctypes

class Array: 
    def __init__( self, size ):
        assert size > 0, 'the size of Array must be greater than 0'
        self._size = size
        arrayTypes = ctypes.py_object * size
        self._array = arrayTypes()
        self.clear( None )


    def __len__( self ):
        return self._size


    def __getitem__( self, index ):
        assert index >= 0 and index < len(self), 'index out of range'
        return self._array[ index ]


    def __setitem__( self, index, value ):
        assert index >= 0 and index < len(self), 'index out of range'
        self._array[ index ] = value


    def clear( self, value ):
        for i in range( len(self) ):
            self._array[i] = value


    def __iter__( self ):
        return _ArrayIterator( self._array )


class _ArrayIterator:
    def __init__( self, theArray ):
        self._arrayRef = theArray
        self._curIndex = 0


    def __iter__( self ):
        return self


    def __next__( self ):
        if self._curIndex < len(self._arrayRef):
            entry = self._arrayRef[self._curIndex]
            self._curIndex += 1
            return entry
        else:
            raise StopIteration