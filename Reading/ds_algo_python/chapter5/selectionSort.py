def selectionSort( theArray ):
    for i in range( len(theArray) - 1 ):
        smallestNdx = i
        for j in range( i+1, len(theArray) ):
            if theArray[j] < theArray[smallestNdx]:
                smallestNdx = j
        
        if smallestNdx != i:
            theArray[i], theArray[smallestNdx] = theArray[smallestNdx], theArray[i]


A = [9, 3, 1, 2, 3, 4, 5, 6, 23, 4, 5, 6]

selectionSort(A)

print(A)