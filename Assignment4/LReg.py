# Student Name: Zach Jagoda
# Student ID: 2274813
# Student Email: jagod101@mail.chapman.edu
# CPSC392 Introduction to Data Science
# Assignment 4: Linear Regression
# Worked with Goldie Malamud 

import math

NUM_ATTRIBUTES = 2
TRAIN_DATA_FILE = "reg_train.csv"


#read the train file and return the data as two lists (ind and dep variables)
def readData(fname):
	data = []
	x = []
	y = []
	f = open(fname,"r")
	for i in f:
		instance = i.split(",")
		x.append(float(instance[0].strip()))
		y.append(float(instance[1].strip()))

	f.close()
	data.append(x)
	data.append(y)
	return data

def printParams(params):
	print("The value of B0 (intercept) is: ", params[0])
	print("The value of B1 (slope) is: ", params[1])

#The linear regression algorithm. Takes a list of lists as input
# x originally ind_variable, y originally dep_variable
def lreg(x,y):
    params = []
    B0 = 0.0
    B1 = 0.0
    
    #Numerator and Denominator Values for B1
    num = 0.0
    den = 0.0
    
    #estimate the linear regression parameters (B0 and B1) here
    xbar = sum(x)/len(x)
    ybar = sum(y)/len(y)
    
    #Iterate through the length of X and calculate the Numerator, Denominator, and B1
    for i in range(len(x)):
        num += x[i] * (y[i] - ybar)
        den += x[i] * (x[i] - xbar)
        B1 = num / den
    
    #Using the Value calculated in B1, Calculate B0    
    B0 = ybar - (B1 * xbar)
    
    #Append the Results of the Linear Regression
    params.append(B0)
    params.append(B1)
    return params


#this is the main routine of the program. You should not have to modify anything here
if __name__ == "__main__":
	train_matrix = readData(TRAIN_DATA_FILE)
	parameters = lreg(train_matrix[0],train_matrix[1])
	printParams(parameters)