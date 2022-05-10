###########################
# TREE SEARCH ALGORITHM   #
#                         #
# This program uses two   #
# search algorithms on    #
# a tree defined by a     #
# simple maze and the     #
# possible paths a person #
# can take.               #
###########################

# The tree we are using our
# search algorithms on.
mazeTree = {
'A': ['C', 'B'],
'B': [],
'C': ['D', 'E'],
'D': [],
'E': ['G', 'F'],
'F': [],
'G': ['H', 'I'],
'H': [],
'I': ['J', 'K'],
'J': [],
'K': ['L', 'M'],
'L': [],
'M': []
}

# A way to check if a node has
# been visited by the searches
visitedNodes = []
visitedNodes2 = []

# The queue of nodes to be added
# to the list by breadth first search.
queue = []

#################################################
# breadthFirstSeach(visitedNodes, tree, root)   #
#                                               #
# visitedNodes - The nodes that have already    #
#                been visited by the function.  #
#                                               #
# tree - The tree that we will be performing    #
#        the search on.                         #
#                                               #
# root - The first node of the tree.            #
#################################################

def breadthFirstSearch(visitedNodes, tree, root):
	# We start by appending the root to both
	# the visitedNodes list and queue
	visitedNodes.append(root)
	queue.append(root)
	
	# The final list
	lst = []

	# While the queue has stuff in it...
	while queue:
		# Take the first node in the queue
		currentNode = queue.pop(0)
		# Add the node to the list
		lst.append(currentNode)
		
		# If the current node has children...
		for child in tree[currentNode]:
			# and if it's not visited...
			if child not in visitedNodes:
				# append the child to visitedNodes,
				visitedNodes.append(child)
				# and add it to the queue for later.
				queue.append(child)

	return lst

# This is just a view of the tree that is displayed to the terminal	
print("-----VIEW OF MAZE TREE-----\n")
print("           A\n")
print("          / \ \n")
print("         C   B\n")
print("        / \ \n")
print("       D   E\n")
print("          / \ \n")
print("         G   F\n")
print("        / \ \n")
print("       H   I\n")
print("          / \ \n")
print("         J   K\n")
print("            / \ \n")
print("           L   M\n")

print("The result of the breadth first search is: \n")
print(breadthFirstSearch(visitedNodes, mazeTree, "A"))
print("\n")

##########################################
# depthFirstSearch(visited, tree, node)  #
#                                        #
# visited - A list of nodes that have    #
#           already been visited by the  #
#           algorithm.                   #
#                                        #
# tree - The tree that we will           #
#        search.                         #
#                                        #
# root - The node that we are            #
#        currently pointing to.          #
##########################################

# A list that holds our results of the depth first search
lst = []

def depthFirstSearch(visited, tree, node):
	# If the node being checked isn't in the visited list...
	if node not in visitedNodes2:
		# add it to the list
		lst.append(node)
		# For every child of the current node being checked...
		for child in tree[node]:
			# recursively go down the tree and search the child
			depthFirstSearch(visitedNodes2, mazeTree, child) 
	return lst

print("The result of the depth first search is: \n")
print(depthFirstSearch(visitedNodes2, mazeTree, 'A'))
