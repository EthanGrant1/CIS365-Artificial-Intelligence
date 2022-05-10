# PERCEPTRON LEARNING ALGORITHM
#
# This program uses a perceptron learning algorithm to find
# the weights to use on a particular function's inputs. In
# this example, we are working with the inputs for a 2-bit
# AND gate.

# Used for the weight randomization
import numpy as np

# The inputs for a 2-bit AND gate
inputs = {
0: [0, 0],
1: [0, 1],
2: [1, 0],
3: [1, 1]
}

# The desired output that we want
desired = {
0: 0,
1: 0,
2: 0,
3: 1
}

# The weights that we will be training on
weights = { }

# The values for y. It is essentially the F(x) of our function, given the inputs.
y_vals = { }

# Corrects the weights by adjusting the old weight and using a learning rate (which we define)
def correct(old, i):
	# The new value is adjusted using the equation below
	new = old[i] + 0.02 * (desired[i] - y_vals[i])

	# For each value in the input
	for j in range(0, len(inputs[i])):
		# Multiply it to the new weight vector
		new *= inputs[i][j]

	# The new weight value
	old[i] = new

# Calculates the y values given our current weights and the inputs.
def find_y(weights, inputs):

	# For all inputs...
	for i in range(0, len(inputs)):
		
		# The sigma value (what we use to determine the fitness for our weight)
		sig = 0.0

		# The dot product of weights and input values gets added to sigma
		for j in range(0, len(inputs[i])):
			sig += weights[i]*inputs[i][j]
		print ("Sigma: " + str(sig))

		# Add bias value. (-0.5)
		sig += -0.5

		# If sigma is > 0...
		if (sig > 0):
			# The y value for that weight is fit
			y_vals[i] = 1
		else:
			# Else, it is not fit
			y_vals[i] = 0
	return y_vals

# Our perceptron learning algorithm, given our inputs
def perceptron(inputs):

	print ("PERCEPTRON LEARNING ALGORITHM\n-----------------------------\n")

	# The total number of steps that it took to adjust the weights
	epochs = 0
	
	# Generate some random weights
	weights = np.random.rand(4,)
	print ("Random weights: " + str(weights))

	# Are all the y values not equal to the predicted values?
	not_all_equal = True

	# Calculate our y values given the random weights
	y_vals = find_y(weights, inputs)
	print ("y_vals: " + str(y_vals))
	
	# While all y values are not equal to the predicted values
	# i.e. we haven't trained enough yet...
	while (not_all_equal):
		# Assume all values are equal from the start
		equal = True

		# For all input values...
		for i in range(0, len(inputs)):
			# Calculate the y values with the current weights
			y_vals = find_y(weights, inputs)
			print("y_vals: " + str(y_vals))

			# If we do not have the desired y value...
			if (y_vals[i] != desired[i]):
				# Correct the weight
				correct(weights, i)
				print ("New weights: " + str(weights))
									
				# All y values are no longer equal
				equal = False
			else:
				# Else, go to the next input and check again
				continue 

		# After weight adjustment, add one to the epoch count
		epochs += 1

		# If all y values are equal to the desired values...
		if (equal == True):
			not_all_equal = False
	

	# The network has been successfully trained!
	print ("\n----------------------------------------------------\n")
	print ("Successfully trained!")
	print ("Desired: " + str(desired))
	print ("Final weights: " + str(weights))
	print ("Final values: " + str(y_vals))
	print ("Epochs: " + str(epochs))
	return

perceptron(inputs)
