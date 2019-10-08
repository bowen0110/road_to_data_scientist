from array import Array
import random

arrayList = Array( 100 )

for i in range( len( arrayList ) ):
    arrayList[ i ] = random.random()

for item in arrayList:
    print( item )

theCounters = Array( 127 )
theCounters.clear( 0 )

theFile = open( 'chapterTwo/textFile.txt', 'r' )
for line in theFile:
    for letter in line:
        code = ord(letter)
        theCounters[code] += 1
theFile.close()

for i in range(26):
    print( '%c - %4d, %c - %4d' %\
        (chr(65+i), theCounters[65+i], chr(97+i), theCounters[97+i]) )

