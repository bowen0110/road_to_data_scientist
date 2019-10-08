from sparse_matrix_linkedlist_version import SparseMatrixLinkedList

M = SparseMatrixLinkedList(3, 2)
M[0, 1] = 1
M[2, 0] = 5.5 
M.scaleBy(3)


def printMatrix(matrix):
    numRows = matrix.numRows()
    numCols = matrix.numCols()
    for m in range(numRows):
        rowValue = []
        for n in range(numCols):
            rowValue.append(matrix[m, n])
        print(rowValue)


printMatrix(M)