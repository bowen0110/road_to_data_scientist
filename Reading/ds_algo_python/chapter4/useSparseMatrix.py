from sparseMatrix import SparseMatrix

M = SparseMatrix(10, 10)
M[2, 3] = 5
print( M[2, 3] )

K = SparseMatrix(10, 10)
K[3, 3] = 5
A = K+M
A.scaleBy(10)

for entry in A._entryList:
    print(entry._value, entry._row, entry._col)

B = K - M

print ( A[2, 3] )
print ( B[2, 3] )
