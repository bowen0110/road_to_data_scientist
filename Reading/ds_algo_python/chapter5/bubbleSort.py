def bubbleSort( theArray ):
    i = len( theArray ) - 1
    while i != 0:
        for j in range(i):
            if theArray[j] > theArray[j+1]:
                theArray[j], theArray[j+1] = theArray[j+1], theArray[j]
        i -= 1

    #for i in range( len(theArray) - 1 ):
    #    for j in range( len(theArray) - i - 1 ):
    #        if theArray[j] > theArray[j+1]:
    #            theArray[j], theArray[j+1] = theArray[j+1], theArray[j]


A = [9, 3, 1, 2, 3, 4, 5, 6, 23, 4, 5, 6]

bubbleSort(A)

print(A)