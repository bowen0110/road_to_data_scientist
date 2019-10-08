def mergeSortedList( listA, listB ):
    a, b = 0, 0
    newList = list()

    while a<len(listA) and b<len(listB):
        if listA[a]<listB[b]:
            newList.append(listA[a])
            a+=1
        else:
            newList.append(listB[b])
            b+=1
    
    if a<len(listA):
        newList.extend(listA[a:])
    
    if b<len(listB):
        newList.extend(listB[b:])

    return newList



A = [1, 2, 3, 4, 6, 9, 10, 12, 23]

B = [2, 4, 5, 6, 9, 10, 49, 234]

result = mergeSortedList(A, B)
print( result )

