####################################
# BAYESIAN CLASSIFIER              #
# --------------------             #
# This program implements a        #
# Bayesian Classifier on an iris   #
# flower data set using one        #
# feature                          #
####################################

# The iris dataset that we are using
# the Bayesian Classifier on. We will
# be testing feature 3 (petal length).

iris_dict = {
1: [5.1,3.5,1.4,0.2,'Iris-setosa'],
2: [4.9,3.0,1.4,0.2,'Iris-setosa'],
3: [4.7,3.2,1.3,0.2,'Iris-setosa'],
4: [4.6,3.1,1.5,0.2,'Iris-setosa'],
5: [5.0,3.6,1.4,0.2,'Iris-setosa'],
6: [5.4,3.9,1.7,0.4,'Iris-setosa'],
7: [4.6,3.4,1.4,0.3,'Iris-setosa'],
8: [5.0,3.4,1.5,0.2,'Iris-setosa'],
9: [4.4,2.9,1.4,0.2,'Iris-setosa'],
10: [4.9,3.1,1.5,0.1,'Iris-setosa'],
11: [5.4,3.7,1.5,0.2,'Iris-setosa'],
12: [4.8,3.4,1.6,0.2,'Iris-setosa'],
13: [4.8,3.0,1.4,0.1,'Iris-setosa'],
14: [4.3,3.0,1.1,0.1,'Iris-setosa'],
15: [5.8,4.0,1.2,0.2,'Iris-setosa'],
16: [5.7,4.4,1.5,0.4,'Iris-setosa'],
17: [5.4,3.9,1.3,0.4,'Iris-setosa'],
18: [5.1,3.5,1.4,0.3,'Iris-setosa'],
19: [5.7,3.8,1.7,0.3,'Iris-setosa'],
20: [5.1,3.8,1.5,0.3,'Iris-setosa'],
21: [5.4,3.4,1.7,0.2,'Iris-setosa'],
22: [5.1,3.7,1.5,0.4,'Iris-setosa'],
23: [4.6,3.6,1.0,0.2,'Iris-setosa'],
24: [5.1,3.3,1.7,0.5,'Iris-setosa'],
25: [4.8,3.4,1.9,0.2,'Iris-setosa'],
26: [5.0,3.0,1.6,0.2,'Iris-setosa'],
27: [5.0,3.4,1.6,0.4,'Iris-setosa'],
28: [5.2,3.5,1.5,0.2,'Iris-setosa'],
29: [5.2,3.4,1.4,0.2,'Iris-setosa'],
30: [4.7,3.2,1.6,0.2,'Iris-setosa'],
31: [4.8,3.1,1.6,0.2,'Iris-setosa'],
32: [5.4,3.4,1.5,0.4,'Iris-setosa'],
33: [5.2,4.1,1.5,0.1,'Iris-setosa'],
34: [5.5,4.2,1.4,0.2,'Iris-setosa'],
35: [4.9,3.1,1.5,0.1,'Iris-setosa'],
36: [5.0,3.2,1.2,0.2,'Iris-setosa'],
37: [5.5,3.5,1.3,0.2,'Iris-setosa'],
38: [4.9,3.1,1.5,0.1,'Iris-setosa'],
39: [4.4,3.0,1.3,0.2,'Iris-setosa'],
40: [5.1,3.4,1.5,0.2,'Iris-setosa'],
41: [5.0,3.5,1.3,0.3,'Iris-setosa'],
42: [4.5,2.3,1.3,0.3,'Iris-setosa'],
43: [4.4,3.2,1.3,0.2,'Iris-setosa'],
44: [5.0,3.5,1.6,0.6,'Iris-setosa'],
45: [5.1,3.8,1.9,0.4,'Iris-setosa'],
46: [4.8,3.0,1.4,0.3,'Iris-setosa'],
47: [5.1,3.8,1.6,0.2,'Iris-setosa'],
48: [4.6,3.2,1.4,0.2,'Iris-setosa'],
49: [5.3,3.7,1.5,0.2,'Iris-setosa'],
50: [5.0,3.3,1.4,0.2,'Iris-setosa'],
51: [7.0,3.2,4.7,1.4,'Iris-versicolor'],
52: [6.4,3.2,4.5,1.5,'Iris-versicolor'],
53: [6.9,3.1,4.9,1.5,'Iris-versicolor'],
54: [5.5,2.3,4.0,1.3,'Iris-versicolor'],
55: [6.5,2.8,4.6,1.5,'Iris-versicolor'],
56: [5.7,2.8,4.5,1.3,'Iris-versicolor'],
57: [6.3,3.3,4.7,1.6,'Iris-versicolor'],
58: [4.9,2.4,3.3,1.0,'Iris-versicolor'],
59: [6.6,2.9,4.6,1.3,'Iris-versicolor'],
60: [5.2,2.7,3.9,1.4,'Iris-versicolor'],
61: [5.0,2.0,3.5,1.0,'Iris-versicolor'],
62: [5.9,3.0,4.2,1.5,'Iris-versicolor'],
63: [6.0,2.2,4.0,1.0,'Iris-versicolor'],
64: [6.1,2.9,4.7,1.4,'Iris-versicolor'],
65: [5.6,2.9,3.6,1.3,'Iris-versicolor'],
66: [6.7,3.1,4.4,1.4,'Iris-versicolor'],
67: [5.6,3.0,4.5,1.5,'Iris-versicolor'],
68: [5.8,2.7,4.1,1.0,'Iris-versicolor'],
69: [6.2,2.2,4.5,1.5,'Iris-versicolor'],
70: [5.6,2.5,3.9,1.1,'Iris-versicolor'],
71: [5.9,3.2,4.8,1.8,'Iris-versicolor'],
72: [6.1,2.8,4.0,1.3,'Iris-versicolor'],
73: [6.3,2.5,4.9,1.5,'Iris-versicolor'],
74: [6.1,2.8,4.7,1.2,'Iris-versicolor'],
75: [6.4,2.9,4.3,1.3,'Iris-versicolor'],
76: [6.6,3.0,4.4,1.4,'Iris-versicolor'],
77: [6.8,2.8,4.8,1.4,'Iris-versicolor'],
78: [6.7,3.0,5.0,1.7,'Iris-versicolor'],
79: [6.0,2.9,4.5,1.5,'Iris-versicolor'],
80: [5.7,2.6,3.5,1.0,'Iris-versicolor'],
81: [5.5,2.4,3.8,1.1,'Iris-versicolor'],
82: [5.5,2.4,3.7,1.0,'Iris-versicolor'],
83: [5.8,2.7,3.9,1.2,'Iris-versicolor'],
84: [6.0,2.7,5.1,1.6,'Iris-versicolor'],
85: [5.4,3.0,4.5,1.5,'Iris-versicolor'],
86: [6.0,3.4,4.5,1.6,'Iris-versicolor'],
87: [6.7,3.1,4.7,1.5,'Iris-versicolor'],
88: [6.3,2.3,4.4,1.3,'Iris-versicolor'],
89: [5.6,3.0,4.1,1.3,'Iris-versicolor'],
90: [5.5,2.5,4.0,1.3,'Iris-versicolor'],
91: [5.5,2.6,4.4,1.2,'Iris-versicolor'],
92: [6.1,3.0,4.6,1.4,'Iris-versicolor'],
93: [5.8,2.6,4.0,1.2,'Iris-versicolor'],
94: [5.0,2.3,3.3,1.0,'Iris-versicolor'],
95: [5.6,2.7,4.2,1.3,'Iris-versicolor'],
96: [5.7,3.0,4.2,1.2,'Iris-versicolor'],
97: [5.7,2.9,4.2,1.3,'Iris-versicolor'],
98: [6.2,2.9,4.3,1.3,'Iris-versicolor'],
98: [5.1,2.5,3.0,1.1,'Iris-versicolor'],
99: [5.7,2.8,4.1,1.3,'Iris-versicolor'],
100: [6.3,3.3,6.0,2.5,'Iris-virginica'],
101: [5.8,2.7,5.1,1.9,'Iris-virginica'],
102: [7.1,3.0,5.9,2.1,'Iris-virginica'],
103: [6.3,2.9,5.6,1.8,'Iris-virginica'],
104: [6.5,3.0,5.8,2.2,'Iris-virginica'],
105: [7.6,3.0,6.6,2.1,'Iris-virginica'],
106: [4.9,2.5,4.5,1.7,'Iris-virginica'],
107: [7.3,2.9,6.3,1.8,'Iris-virginica'],
108: [6.7,2.5,5.8,1.8,'Iris-virginica'],
109: [7.2,3.6,6.1,2.5,'Iris-virginica'],
110: [6.5,3.2,5.1,2.0,'Iris-virginica'],
111: [6.4,2.7,5.3,1.9,'Iris-virginica'],
112: [6.8,3.0,5.5,2.1,'Iris-virginica'],
113: [5.7,2.5,5.0,2.0,'Iris-virginica'],
114: [5.8,2.8,5.1,2.4,'Iris-virginica'],
115: [6.4,3.2,5.3,2.3,'Iris-virginica'],
116: [6.5,3.0,5.5,1.8,'Iris-virginica'],
117: [7.7,3.8,6.7,2.2,'Iris-virginica'],
118: [7.7,2.6,6.9,2.3,'Iris-virginica'],
119: [6.0,2.2,5.0,1.5,'Iris-virginica'],
120: [6.9,3.2,5.7,2.3,'Iris-virginica'],
121: [5.6,2.8,4.9,2.0,'Iris-virginica'],
122: [7.7,2.8,6.7,2.0,'Iris-virginica'],
123: [6.3,2.7,4.9,1.8,'Iris-virginica'],
124: [6.7,3.3,5.7,2.1,'Iris-virginica'],
125: [7.2,3.2,6.0,1.8,'Iris-virginica'],
126: [6.2,2.8,4.8,1.8,'Iris-virginica'],
127: [6.1,3.0,4.9,1.8,'Iris-virginica'],
128: [6.4,2.8,5.6,2.1,'Iris-virginica'],
129: [7.2,3.0,5.8,1.6,'Iris-virginica'],
130: [7.4,2.8,6.1,1.9,'Iris-virginica'],
131: [7.9,3.8,6.4,2.0,'Iris-virginica'],
132: [6.4,2.8,5.6,2.2,'Iris-virginica'],
133: [6.3,2.8,5.1,1.5,'Iris-virginica'],
134: [6.1,2.6,5.6,1.4,'Iris-virginica'],
135: [7.7,3.0,6.1,2.3,'Iris-virginica'],
136: [6.3,3.4,5.6,2.4,'Iris-virginica'],
137: [6.4,3.1,5.5,1.8,'Iris-virginica'],
138: [6.0,3.0,4.8,1.8,'Iris-virginica'],
139: [6.9,3.1,5.4,2.1,'Iris-virginica'],
140: [6.7,3.1,5.6,2.4,'Iris-virginica'],
141: [6.9,3.1,5.1,2.3,'Iris-virginica'],	
142: [5.8,2.7,5.1,1.9,'Iris-virginica'],
143: [6.8,3.2,5.9,2.3,'Iris-virginica'],
144: [6.7,3.3,5.7,2.5,'Iris-virginica'],
145: [6.7,3.0,5.2,2.3,'Iris-virginica'],
146: [6.3,2.5,5.0,1.9,'Iris-virginica'],
147: [6.5,3.0,5.2,2.0,'Iris-virginica'],
148: [6.2,3.4,5.4,2.3,'Iris-virginica'],
149: [5.9,3.0,5.1,1.8,'Iris-virginica'] 
}

import math
import numpy
import statistics

# The Gaussian Density function, using x as the function variable
# as well as being given the standard deviation and mean.
def gau_density(x, std_dev, mean):
	return (numpy.pi*std_dev) * numpy.exp(-0.5*((x-mean)/std_dev)**2)

# Lists to place our training data	
trainDatA = []
trainDatB = []
trainDatC = []

# Creating lists for training data
for i in range(1, 29):
	trainDatA.append(iris_dict[i][0])
		
for i in range(51, 79):
	trainDatB.append(iris_dict[i][0])

for i in range(100, 129):
	trainDatC.append(iris_dict[i][0])

# Means for training data
meanA = statistics.mean(trainDatA)
meanB = statistics.mean(trainDatB)
meanC = statistics.mean(trainDatC)

# Standard deviation for training data
devA = numpy.std(trainDatA)
devB = numpy.std(trainDatB)
devC = numpy.std(trainDatC)

# bayesian()
# -------------------------------------------------------------
# Returns the prediction for a particular class of Iris
# (there are 3 possible classes) using a naive Bayesian
# Classifer. Using the Gaussian Density function, we can
# determine the likelihood of any given value of a particular
# feature (petal length was chosen for this demonstration) and
# then pick which class has the highest likelyhood of occurring.
# --------------------------------------------------------------
def bayesian():
	# Probability of each class
	# A = setosa, B = versicolor, C = viginica
	probA = 0
	probB = 0
	probC = 0

	# The number of correct or incorrect classifications for each class
	correctA = 0
	incorrectA = 0
	correctB = 0
	incorrectB = 0
	correctC = 0
	incorrectC = 0

	# Selecting from our test data
	for i in range(30, 50):
		# Perform the Gaussian density function using each class' mean and std. deviation.
		probA = gau_density(iris_dict[i][0], devA, meanA)
		probB = gau_density(iris_dict[i][0], devB, meanB)
		probC = gau_density(iris_dict[i][0], devC, meanC)

		print("Probability of Iris-setosa: " + str(probA))
		print("Probability of Iris-versicolor: " + str(probB))
		print("Probability of Iris-virginica: " + str(probC) + "\n")

		# Whichever probability is bigger, pick that that class.

		# Iris-setosa
		if ((probA > probB) and (probA > probC)):
			print ("Iris classified as 'Iris-setosa'.")
			print ("Actual classification: " + str(iris_dict[i][4]) + "\n")
			
			if (str(iris_dict[i][4]) == 'Iris-setosa'):
				correctA += 1
			else:
				incorrectA += 1

		# Iris-versicolor
		elif ((probB > probA) and (probB > probC)):
			print ("Iris classified as 'Iris-versicolor'.")
			print ("Actual classification: " + str(iris_dict[i][4]) + "\n")

			if (str(iris_dict[i][4]) == 'Iris-versicolor'):
				correctB += 1
			else:
				incorrectB += 1


		# Iris-virginica
		elif ((probC > probA) and (probC > probB)):
			print ("Iris classified as 'Iris-virginica'.")
			print ("Actual classification: " + str(iris_dict[i][4]) + "\n")

			if (str(iris_dict[i][4]) == 'Iris-virginica'):
				correctC += 1
			else:
				incorrectC += 1

	for i in range(80, 99):
		# Perform the Gaussian density function using each class' mean and std. deviation.
		probA = gau_density(iris_dict[i][0], devA, meanA)
		probB = gau_density(iris_dict[i][0], devB, meanB)
		probC = gau_density(iris_dict[i][0], devC, meanC)

		print("Probability of Iris-setosa: " + str(probA))
		print("Probability of Iris-versicolor: " + str(probB))
		print("Probability of Iris-virginica: " + str(probC) + "\n")

		# Whichever probability is bigger, pick that that class.

		# Iris-setosa
		if ((probA > probB) and (probA > probC)):
			print ("Iris classified as 'Iris-setosa'.")
			print ("Actual classification: " + str(iris_dict[i][4]) + "\n")
			
			if (str(iris_dict[i][4]) == 'Iris-setosa'):
				correctA += 1
			else:
				incorrectA += 1

		# Iris-versicolor
		elif ((probB > probA) and (probB > probC)):
			print ("Iris classified as 'Iris-versicolor'.")
			print ("Actual classification: " + str(iris_dict[i][4]) + "\n")

			if (str(iris_dict[i][4]) == 'Iris-versicolor'):
				correctB += 1
			else:
				incorrectB += 1


		# Iris-virginica
		elif ((probC > probA) and (probC > probB)):
			print ("Iris classified as 'Iris-virginica'.")
			print ("Actual classification: " + str(iris_dict[i][4]) + "\n")

			if (str(iris_dict[i][4]) == 'Iris-virginica'):
				correctC += 1
			else:
				incorrectC += 1


	for i in range(130, 149):
		# Perform the Gaussian density function using each class' mean and std. deviation.
		probA = gau_density(iris_dict[i][0], devA, meanA)
		probB = gau_density(iris_dict[i][0], devB, meanB)
		probC = gau_density(iris_dict[i][0], devC, meanC)

		print("Probability of Iris-setosa: " + str(probA))
		print("Probability of Iris-versicolor: " + str(probB))
		print("Probability of Iris-virginica: " + str(probC) + "\n")

		# Whichever probability is bigger, pick that that class.

		# Iris-setosa
		if ((probA > probB) and (probA > probC)):
			print ("Iris classified as 'Iris-setosa'.")
			print ("Actual classification: " + str(iris_dict[i][4]) + "\n")
			
			if (str(iris_dict[i][4]) == 'Iris-setosa'):
				correctA += 1
			else:
				incorrectA += 1

		# Iris-versicolor
		elif ((probB > probA) and (probB > probC)):
			print ("Iris classified as 'Iris-versicolor'.")
			print ("Actual classification: " + str(iris_dict[i][4]) + "\n")

			if (str(iris_dict[i][4]) == 'Iris-versicolor'):
				correctB += 1
			else:
				incorrectB += 1


		# Iris-virginica
		elif ((probC > probA) and (probC > probB)):
			print ("Iris classified as 'Iris-virginica'.")
			print ("Actual classification: " + str(iris_dict[i][4]) + "\n")

			if (str(iris_dict[i][4]) == 'Iris-virginica'):
				correctC += 1
			else:
				incorrectC += 1

	print ("Correct classifications for Iris-setosa: " + str(correctA))
	print ("Incorrect classifications for Iris-setosa: " + str(incorrectA) + "\n")

	print ("Correct classifications for Iris-versicolor: " + str(correctB))
	print ("Incorrect classifications for Iris-versicolor: " + str(incorrectB) + "\n")

	print ("Correct classifications for Iris-virginica: " + str(correctC))
	print ("Incorrect classifications for Iris-virginica: " + str(incorrectC) + "\n")

print (bayesian())
