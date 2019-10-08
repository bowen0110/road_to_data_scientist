def insertionSort( theArray ):
    #for i in range( len(theArray) ):
    #    for j in range( len(theArray[:i]) ):
    #        if theArray[i] < theArray[j]:
    #            value = theArray.pop(i)
    #            theArray.insert(j, value)

    for i in range( 1, len(theArray) ):
        value = theArray[i]
        pos = i
        while pos > 0 and value < theArray[pos-1]:
            theArray[pos] = theArray[pos-1]
            pos -= 1
        theArray[pos] = value

A = [9,2,1,2,3,4,42,2,1,3,4,2,33,45,23,0,-1]

insertionSort(A)

print(A)