# Student Name: Zach Jagoda
# Student ID: 2274813
# Student Email: jagod101@mail.chapman.edu
# CPSC392 Introduction to Data Science
# Assignment 5: InfoGain and Entropy
# Worked with Goldie Malamud 

import math

#valueSplit is a list of 2 items. The first is number of positive examples,
#the second is the number of negative examples
def calcEntropy(valueSplit):
    h = 0.0
    h1 = valueSplit[0]
    h2 = valueSplit[1]
    total = valueSplit[0] + valueSplit[1]
    
    prob1 = h1/total
    prob2 = h2/total
    
    h = -(prob1 * math.log(prob1, 2)) - (prob2 * math.log(prob2, 2))
    
    return h

#rootValues is a list of the values at the parent node. It consists of 2 items.
#The first is number of positive examples,
#the second is the number of negative examples
#descendantValues is a list of lists.  Each inner list consists of the number of positive
#and negative examples for the attribute value you want to split on.
def calcInfoGain(rootValues,descendantValues):
    gain = 0.0
    infoGain = 0.0
    total = 0
    rootEntropy = calcEntropy(rootValues)
    
    for x in descendantValues:
        total += sum(x)
        
    for y in descendantValues:
        infoGain += -(sum(y)/total * calcEntropy(y))
    
    gain = calcEntropy(rootValues) + infoGain
    
    return gain



if __name__ == "__main__":
    attributeName = "Humidity"
    rootSplit = [9,5] # 9 positive, 5 negative examples
    descendantSplit = [[3,4],[6,1]]
    
    ig = calcInfoGain(rootSplit, descendantSplit)
    print("The information gain of splitting on ",attributeName," is: ",ig," bits")