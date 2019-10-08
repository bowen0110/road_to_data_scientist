class StudentFileReader:

    def __init__(self, fileSrc):
        self._fileSrc = fileSrc
        self._fileInput = None

    def open(self):
        self._fileInput = open(self._fileSrc, 'r')
    
    def close(self):
        self._fileInput.close()
        self._fileInput = None
  
    def fetchAll(self):
        records = list()
        studentRecord = self.fetchRecord()
        while studentRecord:
            records.append(studentRecord)
            studentRecord = self.fetchRecord()
        return records

    def fetchRecord(self):
        line = self._fileInput.readline()
        if line == ' ':
            return None 
        
        student = StudentRecord()
        student.idNum = int(line)
        student.firstName = self._fileInput.readline().rstrip()
        student.lastName = self._fileInput.readline().rstrip()
        student.classCode = int(self._fileInput.readline())
        student.gpa = float(self._fileInput.readline())
        return student


class StudentRecord:

    def __init__(self):
        self.idNum = 0
        self.firstName = None
        self.lastName = None
        self.classCode = 0
        self.gpa = 0.0

