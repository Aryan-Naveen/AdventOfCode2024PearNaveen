# read the list 
# split the list into two seperate lists
# sort both lists from least to greatest
# sum each list starting from least to greatest
#take total sum of each list distance
import numpy as np
import math
# Load data from a text file
data = np.loadtxt('day1', delimiter=' ' , dtype=float)

column1 = data[: , 0]
column2 = data[: , 1]

column1.sort()
column2.sort()

sscore = 0
totalss = 0
for num in column1:
    sscore = list(column2).count(num)
    sscore *= num
    totalss += sscore
print (totalss)