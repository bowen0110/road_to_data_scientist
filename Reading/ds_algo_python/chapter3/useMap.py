from listBasedMap import Map

M = Map()
M.add(1, 'peter')
M.add(2, 'bob')
M.add(3, 'ben')

print( len(M) )

M.remove( 2 )

for key in M:
    print( 2 in M )
    print( key )
    print( M.valueOf(key) )
