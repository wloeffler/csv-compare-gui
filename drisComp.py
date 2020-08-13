import csv
import collections
from Info import inputInfo

class Comparer:

    def __init__(cls, infoPasser):

        csv1 = open(infoPasser.fileNameA)
        csv2 = open(infoPasser.fileNameB)

        """
        legacyCerner = csv.DictReader(csvleg)
        drisExport = csv.DictReader(csvDRIS)
        """
        legacyCerner = csv.reader(csv1)
        drisExport = csv.reader(csv2)

        legAcyList = list()
        newList = list()

        for line in drisExport:
            newList.append(line)
        for line in legacyCerner:
            legAcyList.append(line)

        #calls the new comparision function
        cls.runComparison(legAcyList,newList)
        return


    def runComparison(self,legList, newList):
        outFile = csv.writer(open("missingData.csv", 'w'))
        i = 0
        j = 0
        for oldInfo in legList:
            flag = False
            for newInfo in newList:
                if (collections.Counter(oldInfo) == collections.Counter(newInfo)):
                    flag = True
                 #   print((str(oldInfo)) + '\n')
                  #  print(str(newInfo) + '\n\n')
                    newList.remove(newInfo)
                    break
            if (not flag):
                # outFile.write("line " + str(i) +','+ str(oldInfo[0]) + str(oldInfo[1]) +str(oldInfo[2]) +str(oldInfo[3]) +str(oldInfo[4]) +str(oldInfo[5]) +str(oldInfo[6]) +str(oldInfo[7]) +str(oldInfo[8]) +str(oldInfo[9]) +str(oldInfo[10]) +str(oldInfo[11]) +'\n')
                outFile.writerow(oldInfo)

                j = j + 1
            i = i + 1

        #print(str(i) + '\t' + str(j))

        return





