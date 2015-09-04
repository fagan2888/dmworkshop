# Titanic Gender Model created by Trey Hughs
# This basic model scored 0.76555 accuracy

# imports relevant packages
import csv as csv	# for reading and writing csv files
import numpy as np 	# for maths and arrays
import pandas 		# allows us to use the pandas package

titanic = pandas.read_csv("train.csv") #creates a csv object

#looking at the data
print(titanic.describe()) #prints some statistics of our dataset

# deals with missing data
titanic["Age"] = titanic["Age"].fillna(titanic["Age"].median())

print(titanic.describe()) #you can now see 891 entries for age

#converts one of our non-numeric columns to numeric for later calculations
print(titanic["Sex"].unique()) #find all the unique values for gender
titanic.loc[titanic["Sex"] == "male", "Sex"] = 0
titanic.loc[titanic["Sex"] == "female", "Sex"] = 1

#converts the embarked column to numeric values
#have students do on thier own given an example of the first line
print(titanic["Embarked"].unique()) #find all the unique values for embarked
titanic["Embarked"] = titanic["Embarked"].fillna("S")
titanic.loc[titanic["Embarked"] == "S", "Embarked"] = 0
titanic.loc[titanic["Embarked"] == "C", "Embarked"] = 1
titanic.loc[titanic["Embarked"] == "Q", "Embarked"] = 2
print(titanic["Embarked"].unique()) #check if the changes went through

# opens a csv file into a python object
testFile = open('test.csv', 'rb')
testFileObject = csv.reader(testFile)
header = testFileObject.next()	# skips the first line of csv which is the header

# opens a pointer to a new file (doesn't exist yet)
predictionFile = open("mypredictions.csv", "wb")
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