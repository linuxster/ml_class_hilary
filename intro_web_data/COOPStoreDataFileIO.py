import csv
ReadData=csv.reader(open('Store Clustering Location Attributes.csv','rU'), delimiter=';')

def column(ReadData, i):
    return [row[i] for row in ReadData]

for line in ReadData:
   WriteData=csv.writer(open('Store Clustering Location Attributes Python.csv','wb'),
                        delimiter=',', quotechar=",", quoting=csv.QUOTE_ALL)
   print column(ReadData,1)
