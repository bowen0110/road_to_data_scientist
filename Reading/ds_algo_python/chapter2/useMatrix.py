from .matrix import Matrix

A = Matrix(3, 2)
B = Matrix(2, 3)

N = [i+j for i in range(3) for j in range(2)]
M = [i+j for i in range(2) for j in range(3)]

print( N )


def giveValueToMatrix(aMatrix, numList):
    count = 0
    for row in range(aMatrix.numRows()):
        for col in range(aMatrix.numCols()):
            aMatrix[row, col] = numList[count]
            count += 1

def printMatrix(aMatrix):
    for row in range(aMatrix.numRows()):
        for col in range(aMatrix.numCols()):
            print( aMatrix[row, col], end = ' ' )
        print( '\n' )

#giveValueToMatrix(A, N)
#giveValueToMatrix(B, M)
#printMatrix(A)
#printMatrix(B)
#A.scaleBy(5)
#printMatrix(A*B)