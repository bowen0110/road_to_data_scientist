class Set:
    def __init__( self ):
        self._elements = list()

    def __len__( self ) -> int:
        return len( self._elements )

    def __contains__( self, element ) -> bool:
        return element in self._elements

    def isEmpty( self ) ->bool:
        return len(self) == 0

    def add( self, element: any ):
        if element not in self:
            self._elements.append(element)

    def remove( self, element ):
        assert element in self, 'no such element in set'
        self._elements.remove(element)

    def __eq__( self, setB: 'Set' ) -> bool:
        if len(self) != len(setB):
            return False
        else:
            return self.isSubsetOf(setB)

    def isSubsetOf( self, setB: 'Set' ) -> bool:
        for element in self:
            if element not in setB:
                return False
        return True

    def union( self, setB: 'Set' ) -> 'Set':
        newSet = Set()
        newSet._elements.extend(self._elements)
        for e in setB:
            if e not in newSet:
                newSet.add(e)
        return newSet

    def intersect( self, setB: 'Set' ) -> 'Set':
        newSet = Set()
        for e in self: 
            if e in setB:
                newSet.add(e)
        return newSet

    def difference( self, setB: 'Set' ) -> 'Set':
        newSet = Set()
        for e in self:
            if e not in setB:
                newSet.add(e)
        return newSet
    
    def __iter__( self ) -> '_SetIterator':
        return _SetIterator( self._elements )


class _SetIterator:
    def __init__( self, theElements: list ):
        self._setItems = theElements
        self._curIndex = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._curIndex < len(self._setItems):
            item = self._setItems[self._curIndex]
            self._curIndex += 1
            return item
        else:
            raise StopIteration