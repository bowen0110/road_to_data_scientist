class SortedSet:
    def __init__(self):
        self._theSet = list()

    def __len__(self):
        return len(self._theSet)

    # eq operator
    # this function has o(logn) running time
    def __contains__(self, value):
        Ndx = self._findPosition(value)
        if 0<=Ndx and Ndx<len(self) and self._theSet[Ndx] == value:
            return True
        return False

    # o(logn) + o(n) -> o(n) times
    # insert() has the worst of o(n) 
    # times if copy n elemnts into a new list
    def add(self, value):
        if value not in self:
            Ndx = self._findPosition(value)
            self._theSet.insert(Ndx, value)

    # o(logn) + o(n) -> o(n)
    # pop has worst of o(n) if pop the first element
    def remove(self, value):
        assert value in self, 'value is not in set'
        Ndx = self._findPosition(value)
        self._theSet.pop(Ndx)
    
    # o(n)
    # if two sorted sets are equal, then length are the same
    # and every element on every position must be same
    def __eq__(self, setB):
        if len(self) != len(setB):
            return False
        else:
            for i in range(len(self)):
                if self._theSet[i] != setB._theSet[i]:
                    return False
        return True

    # o(n)
    # traverse all elements in set A
    # if element a is bigger than element b, go to next b
    # if element a is equal element b, go to next a and b
    # if element a is smaller than element b, return false
    # terminate loop if a or b list is traversed over 
    # if there is element left in A not been visited, return false
    # since two sets are in order, then if we visit elements in order
    # if we find a smaller element in A, that means it will never occur in set B
    # then false
    # if we find a bigger element in A, we keep visiting B until we find a same element
    # in B, or we find a bigger element in B to see that A is not a subset
    def isSubsetOf(self, setB):
        if len(self) > len(setB):
            return False
        else:
            a, b = 0, 0
            while a<len(self) and b<len(setB):
                if self._theSet[a]<setB._theSet[b]:
                    return False
                elif self._theSet[a] == setB._theSet[b]:
                    a+=1
                    b+=1
                else:
                    b+=1
            if a<len(self):
                return False
        return True

    # use mergeSortedLists way to merge two sorted sets
    # running time o(n)
    def union(self, setB):
        a, b = 0, 0
        unionList = list()
        while a<len(self) and b<len(setB):
            if self._theSet[a] < setB._theSet[b]:
                unionList.append(self._theSet[a])
                a+=1
            elif self._theSet[a] == setB._theSet[b]:
                unionList.append(self._theSet[a])
                a+=1
                b+=1
            else:
                unionList.append(setB._theSet[b])
                b+=1
        if a<len(self):
            unionList.extend(self._theSet[a:])
        if b<len(setB):
            unionList.extend(setB._theSet[b:])
        return unionList

    # running time o(n)
    def intersect(self, setB):
        a, b = 0, 0
        intersectList = list()
        while a<len(self) and b<len(setB):
            if self._theSet[a] < setB._theSet[b]:
                a+=1
            elif self._theSet[a] == setB._theSet[b]:
                intersectList.append(self._theSet[a])
                a+=1
                b+=1
            else:
                b+=1
        return intersectList

    # running time o(n)
    def difference(self, setB):
        a, b = 0, 0
        differentList = list()
        while a<len(self) and b<len(setB):
            if self._theSet[a] == setB._theSet[b]:
                a+=1
                b+=1
            elif self._theSet[a] < setB._theSet[b]:
                differentList.append(self._theSet[a])
                a+=1
            else:
                b+=1
        if a<len(self):
            differentList.extend(self._theSet[a:])
        return differentList

    # this function uses binary search to find the position
    # of a target value in the set
    # if find value: return the index
    # if not find value, return the index that the value should be inserted in
    # this function is o(logn) running time
    def _findPosition(self, value):
        low, high = 0, len(self._theSet)-1  # o(1)
        while low<=high:                    # loop runs n/2, n/4, n/8... o(logn) times
            mid = (low+high)//2
            if self._theSet[mid] == value:
                return mid
            elif self._theSet[mid] < value:
                low = mid + 1
            else:
                high = mid - 1
        return low

    def __iter__(self):
        return _SortedSetIterator(self._theSet)


class _SortedSetIterator:
    def __init__(self, theSet):
        self._iterList = theSet
        self._curNdx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._curNdx < len(self._iterList):
            item = self._iterList[self._curNdx]
            self._curNdx += 1
            return item
        else:
            raise StopIteration