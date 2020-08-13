"""
This class is used to handle the inforation entered in the UI and pass it to the processing class
"""

class inputInfo:

    def __init__(self, fileNameA, fileNameB):
        #the first file
        self.fileNameA = fileNameA
        #he second file
        self.fileNameB = fileNameB
        #a list of the number of columns from 0 - n
