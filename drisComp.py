import csv
from Info import inputInfo



def __init__(infoPasser):
    csvleg = open(infoPasser.fileNameA)
    csvDRIS = open(infoPasser.fileNameB)
    outFile = csv.writer(open("missingData.csv", 'w'))



"""
legacyCerner = csv.DictReader(csvleg)
drisExport = csv.DictReader(csvDRIS)
"""
legacyCerner = csv.reader(csvleg)
drisExport = csv.reader(csvDRIS)

legAcyList= list()
newList = list()

for line in drisExport:
    newList.append(line)
for line in legacyCerner:
    legAcyList.append(line)

i =0
j =0
for oldInfo in legAcyList:
    flag = False
    for newInfo in newList:
        if ((str(oldInfo[0])+" "+str(oldInfo[1]))==newInfo[0] and oldInfo[2]==newInfo[1] and oldInfo[3]==newInfo[2] and oldInfo[4]==newInfo[3]and oldInfo[5]==newInfo[4]and oldInfo[6]==newInfo[5]and oldInfo[7]==newInfo[6] and oldInfo[-1] == newInfo[-1]):
            flag = True
            print((str(oldInfo))+'\n')
            print(str(newInfo)+'\n\n')
            newList.remove(newInfo)
            break
    if(not flag):
        #outFile.write("line " + str(i) +','+ str(oldInfo[0]) + str(oldInfo[1]) +str(oldInfo[2]) +str(oldInfo[3]) +str(oldInfo[4]) +str(oldInfo[5]) +str(oldInfo[6]) +str(oldInfo[7]) +str(oldInfo[8]) +str(oldInfo[9]) +str(oldInfo[10]) +str(oldInfo[11]) +'\n')
        outFile.writerow(oldInfo)

        j=j+1
    i = i + 1


print(str(i) + '\t' +str(j))


