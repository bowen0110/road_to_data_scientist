from sortedSet import SortedSet

A = SortedSet()
A.add(0)
A.add(4)
A.add(5)
A.add(6)
A.add(2)
A.add(4)
A.add(8)
A.add(49)
A.remove(2)
print(A._theSet)

B = SortedSet()

B.add(1)
B.add(4)
B.add(5)
B.add(6)
B.add(8)
B.add(9)
#print(B._theSet)

C = SortedSet()

C.add(1)
C.add(4)
C.add(5)
C.add(6)
C.add(8)
C.add(49)
print(C._theSet)

#print(A.union(B))
#print(A.intersect(B))
#print(A.difference(B))
#print(A == B)
print(A.isSubsetOf(C))
