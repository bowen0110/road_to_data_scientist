from multiArray import MultiArray

M = MultiArray(3,3,3)

print( [i for i in M._factors] )

print( M._computeIndex( [0, 0, 3] ) )