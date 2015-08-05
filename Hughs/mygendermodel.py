# Titanic Gender Model created by Trey Hughs
# This basic model scored 0.76555 accuracy

# imports relevant packages
import csv as csv	# for reading and writing csv files
import numpy as np 	# for maths and arrays

# opens a csv file into a python object
testFile = open('/home/ugrad4/hhughs/titanic/test.csv', 'rb')
testFileObject = csv.reader(testFile)
header = testFileObject.next()	# skips the first line of csv which is the header

# opens a pointer to a new file (doesn't exist yet)
predictionFile = open("mygenderbasedmodel.csv", "wb")
predictionFileObject = csv.writer(predictionFile)

# reads the test file row by row to see if the passenger is female
# if passenger is female then we predict they survived
predictionFileObject.writerow(["PassengerId", "Survived"])
for row in testFileObject:
	if row[3] == 'female':
		predictionFileObject.writerow([row[0], '1'])	# predict 1
	else:
		predictionFileObject.writerow([row[0], '0'])	# predict 0
testFile.close()
predictionFile.close()
