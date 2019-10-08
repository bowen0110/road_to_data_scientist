class Map:
    def __init__( self ):
        self._mapEntries = list()

    def __len__( self ) -> int:
        return len( self._mapEntries )

    def __contains__( self, key ) -> bool:
        return self._findPosition( key ) is not None
    
    def add( self, key, value ) -> bool:
        index = self._findPosition( key )
        if index is None:
            newEntry = _MapEntry( key, value )
            self._mapEntries.append( newEntry )
            return True
        else:
            self._mapEntries[index]._value = value
            return False

    def remove( self, key ):
        index = self._findPosition( key )
        assert index is not None, 'no such key in Map'
        self._mapEntries.pop( index )
    
    def valueOf( self, key ) -> 'Value of MapEntry':
        index = self._findPosition( key )
        assert index is not None, 'no such key in Map'
        return self._mapEntries[index]._value

    def _findPosition(self, key):
        for index in range( len(self) ):
            if key == self._mapEntries[index]._key:
                return index
        return None
    
    def __iter__( self ):
        return _MapIterator( self._mapEntries )


class _MapEntry:
    def __init__(self, key, value):
        self._key = key
        self._value = value

class _MapIterator:
    def __init__( self, theList ):
        self._mapToIter = theList
        self._curIndex = 0
    
    def __iter__( self ):
        return ( self )

    def __next__( self ):
        if self._curIndex < len( self._mapToIter ):
            item = self._mapToIter[self._curIndex]._key
            self._curIndex += 1
            return item
        else:
            raise StopIteration
            