###########################
#    MINMAX EVALUATOR     #
#    ----------------     #
# This program performs   #
# a minmax evaluation on  #
# a game tree to see if   #
# it results in a win for #
# min or max.             #
###########################

# Note: There are some extra print() statements used for debugging.

# pseudo code
"""
function minmax(list position, int depth, bool maximizingPlayer):
	if (depth == 0 or game is over at current position):
		return staticEval(position)

	if (maximizingPlayer):
		maxEval = -Inf
		for child in position:
			eval = minmax(child, depth - 1, false)
			maxEval = max(maxEval, eval)
		return maxEval

	else:
		minEval = +Inf
		for child in position:
			eval = minmax(child, depth - 1, true)
			min(minEval, eval)
"""

# The graph that we will perform our algortihm on.
game_tree = {
'A': [[-1], ['B', 'C', 'D']],
'B': [[-1], ['E', 'F']],
'C': [[-1], ['G', 'H']],
'D': [[-1], ['I', 'J']],
'E': [[-1], ['K', 'L', 'M']],
'F': [[-1], ['N', 'O']],
'G': [[-1], ['P']],
'H': [[-1], ['Q', 'R']],
'I': [[-1], ['S', 'T']],
'J': [[-1], ['U', 'V']],
'K': [[2], []],
'L': [[1], []],
'M': [[3], []],
'N': [[5], []],
'O': [[4], []],
'P': [[7], []],
'Q': [[6], []],
'R': [[8], []],
'S': [[9], []],
'T': [[10], []],
'U': [[12], []],
'V': [[1], []]
}

# Used for math.inf
import math

# The final result of our evaluations
evaluated = 0

# Just so we can keep track of the indices
index = 0
keylist = {}
for key in game_tree:
	keylist[key] = index
	index += 1

# MinMax(position, depth, isMaxPlayer)
# position - Node that we are currently searching
# depth - How far we have traversed down the tree (i.e. how many generations of children we searched)
# isMaxPlayer - A bool to keep track if it is Max's turn or Min's turn
def MinMax(position, depth, isMaxPlayer):
	childcounter = 0

	print("position, depth, isMaxPlayer: " + str(position) + ', ' + str(depth) + ', ' + str(isMaxPlayer))


#	# Some temp variables to find the current position
#	temp1 = 0
#	temp2 = 'temp'
#	while (temp2 != str(position)):
#		temp2 = str(list(game_tree.keys())[temp1])
#		print('temp2: ' + str(temp2))
#		temp1 += 1
#		print('temp1: ' + str(temp1))

	# Count children of the current node
	for ele in game_tree[position][1]:
		childcounter += 1
#	print('childcounter: ' + str(childcounter))	
	
	# If we have gone to the lowest depth or there are no more children to search
	if (depth == 0 or childcounter == 0):
#		print('Static Eval: ' + str(game_tree[position][0][0]))
		
		# Get the static evaluation number
		evaluated = int(game_tree[position][0][0])
		return evaluated
	
	# If it is Max's turn...
	if (isMaxPlayer == True):
		# Initialize the worst possible score for Max
		maxEval = -math.inf
		# For every child of the current Node
		for child in game_tree[position][1]:
			# Recursively go down a layer
			evaluated = MinMax(list(game_tree.keys())[keylist[child]], depth-1, False)
#			print('evaluated: ' + str(evaluated))

			# Calculate the maximum evaluation
			maxEval = max(maxEval, evaluated)
			print('Best value after maxEval: ' + str(maxEval))
		return maxEval

	# Else, it is Min's turn
	else:
		# Initialize the worst possible score for Min
		minEval = math.inf
		# For every child of the current Node
		for child in game_tree[position][1]:
			# Recursively go down a layer
			evaluated = MinMax(list(game_tree.keys())[keylist[child]], depth-1, True)
#			print('evaluated: ' + str(evaluated))

			# Calculate the minimum evaluation
			minEval = min(minEval, evaluated)
			print ('Best value after minEval: ' + str(minEval))
		return minEval

print("The result of the algorithm assumes optimal play from both sides and will result in the static evalulation score at the end of that search.")
print('The result of the MinMax algorithm on the game_tree is: ' + str(MinMax(list(game_tree.keys())[0], 3, True)))

