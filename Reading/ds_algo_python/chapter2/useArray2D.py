from array2D import Array2D

content = open( 'chapterTwo/theFile.txt', 'r' )

numStudents = int( content.readline() )
numExams = int( content.readline() )

theArray = Array2D( numStudents, numExams )

for i in range(numStudents):
    scores = content.readline().split()
    for j in range(numExams):
        print (scores[j])
        theArray[i, j] = int( scores[j] )
    
content.close()

for i in range(numStudents):
    total = 0
    for j in range(numExams):
        total += theArray[i, j]
    avgScore = total/numExams
    print ('%2d, %6.2f' %(i+1, avgScore) )
