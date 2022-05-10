##################################
# INFORMED SEARCH ALGORITHM      #
# -------------------------      #
# This program uses an informed  #
# search algorithm on a map in   #
# order to find the most optimal #
# path.                          #
##################################

"""
Some quick and dirty ways of printing the map.
The map was later pruned to incorporate walls.

keys = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
new_list = []
map_graph = {}

 for key in keys:
 	for num in nums:
 		temp = key+num
		new_list.append(temp)

for ele in new_list:
 	map_graph[ele] = new_list

print("map_graph = {\n")

for key in map_graph:
	print(key + ":[")
 	temp = ""
 	for ele in map_graph[key]:
 		temp += "'" + ele + "', "
	print(temp + "]")

for num in range(1,7):
	for num2 in range(1,8):
		temp1 = keys[num-1]+nums[num2-1]
		temp2 = keys[num-1]+nums[num2]
		temp3 = keys[num-1]+nums[num2+1]
		temp4 = keys[num]+nums[num2-1]
		temp5 = keys[num]+nums[num2]
		temp6 = keys[num]+nums[num2+1]
		temp7 = keys[num+1]+nums[num2-1]
		temp8 = keys[num+1]+nums[num2]
		temp9 = keys[num+1]+nums[num2+1]
		map_graph[temp5] = []
		map_graph[temp5].append(temp1)
		map_graph[temp5].append(temp2)
		map_graph[temp5].append(temp3)
		map_graph[temp5].append(temp4)
		map_graph[temp5].append(temp6)
		map_graph[temp5].append(temp7)
		map_graph[temp5].append(temp8)
		map_graph[temp5].append(temp9)
		
for key in map_graph:
	print (key + ': ')
	print (map_graph[key])
	print ("\n")
"""

# The map that we will be searching through
map_graph = {
'A1': ['A2', 'B1', 'B2'], 
'A2': ['A1', 'A3', 'B1', 'B2', 'B3'], 
'A3': ['A2', 'A4', 'B2', 'B3', 'B4'], 
'A4': ['A3', 'A5', 'B3', 'B4', 'B5'],
'A5': ['A4', 'A6', 'B4', 'B5', 'B6'], 
'A6': ['A5', 'A7', 'B5', 'B6', 'B7'], 
'A7': ['A6', 'A8', 'B6', 'B7', 'B8'], 
'A8': ['A7', 'A9', 'B7', 'B8', 'B9'],
'A9': ['A8', 'B8', 'B9'],
'B1': ['A1', 'A2', 'B2', 'C1', 'C2'], 
'B2': ['A1', 'A2', 'A3', 'B1', 'B3', 'C1', 'C2', 'C3'], 
'B3': ['A2', 'A3', 'A4', 'B2', 'B4', 'C2', 'C3', 'C4'], 
'B4': ['A3', 'A4', 'A5', 'B3', 'B5', 'C3', 'C4'], 
'B5': ['A4', 'A5', 'A6', 'B4', 'B6', 'C4'], 
'B6': ['A5', 'A6', 'A7', 'B5', 'B7'], 
'B7': ['A6', 'A7', 'A8', 'B6', 'B8'], 
'B8': ['A7', 'A8', 'A9', 'B7', 'B9', 'C9'],
'B9': ['A8', 'A9', 'B8', 'C8', 'C9'],
'C1': ['B1', 'B2', 'C2' 'D1', 'D2'], 
'C2': ['B1', 'B2', 'B3', 'C1', 'C3', 'D1', 'D2', 'D3'], 
'C3': ['B2', 'B3', 'B4', 'C2', 'C4', 'D2', 'D3', 'D4'], 
'C4': ['B3', 'B4', 'B5', 'C3','D3', 'D4'], 
'C5': ['C6', 'D5', 'D6'], 
'C6': ['C5', 'C7', 'D5', 'D6', 'D7'], 
'C7': ['C6', 'D6', 'D7'], 
'C8': ['B9', 'C9', 'D8', 'D9'], 
'C9': ['B8', 'B9', 'C8', 'D8', 'D9'],
'D1': ['C1', 'C2', 'D2', 'E1', 'E2'], 
'D2': ['C1', 'C2', 'C3', 'D1', 'D3', 'E1', 'E2'], 
'D3': ['C2', 'C3', 'C4', 'D2', 'D4', 'E2'],
'D4': ['C3', 'C4', 'D3'], 
'D5': ['C5', 'C6', 'D6', 'E6'], 
'D6': ['C5', 'C6', 'C7', 'D5', 'D7', 'E6', 'E7'],
'D7': ['C6', 'C7', 'D6', 'E6', 'E7', 'E8'],
'D8': ['C8', 'C9', 'D9', 'E7', 'E8', 'E9'], 
'D9': ['C8', 'C9', 'D8', 'E8', 'E9'],
'E1': ['D1', 'D2', 'E2', 'F1', 'F2'], 
'E2': ['D1', 'D2', 'D3', 'E1', 'F1', 'F2'], 
'E3': ['E4', 'F3', 'F4'], 
'E4': ['E3', 'E5', 'F3', 'F4', 'F5'], 
'E5': ['D6', 'E4', 'E6', 'F4', 'F5', 'F6'], 
'E6': ['D5', 'D6', 'D7', 'E5', 'E7', 'F5', 'F6', 'F7'], 
'E7': ['D6', 'D7', 'D8', 'E6', 'E8', 'F6', 'F7', 'F8'], 
'E8': ['D7', 'D8', 'D9', 'E7', 'E9', 'F7', 'F8', 'F9'], 
'E9': ['D8', 'D9', 'E8', 'F8', 'F9'],
'F1': ['E1', 'E2', 'F2', 'G1', 'G2'], 
'F2': ['E1', 'E2', 'F1', 'G1'], 
'F3': ['E3', 'E4', 'F4', 'G2', 'G3', 'G4'], 
'F4': ['E3', 'E4', 'E5', 'F3', 'F5', 'G3', 'G4'], 
'F5': ['E4', 'E5', 'E6', 'F4', 'F6', 'G4'], 
'F6': ['E5', 'E6', 'E7', 'F5', 'F7'], 
'F7': ['E6', 'E7', 'E8', 'F6', 'F8'], 
'F8': ['E7', 'E8', 'E9', 'F7', 'F9', 'G9'], 
'F9': ['E8', 'E9', 'F8', 'G8', 'G9'], 
'G1': ['F1', 'F2', 'G2', 'H1', 'H2'], 
'G2': ['F1', 'F3', 'G1', 'G3', 'H1', 'H2', 'H3'], 
'G3': ['F3', 'F4', 'G2', 'G4', 'H2', 'H3', 'H4'], 
'G4': ['F3', 'F4', 'F5', 'G3', 'H3', 'H4', 'H5'], 
'G5': ['G6', 'H4', 'H5', 'H6'], 
'G6': ['G5', 'G7', 'H5', 'H6', 'H7'], 
'G7': ['G6', 'G8', 'H6', 'H7', 'H8'], 
'G8': ['F9', 'G7', 'G9', 'H7', 'H8', 'H9'],
'G9': ['F8', 'F9', 'G8', 'H8', 'H9'], 
'H1': ['G1', 'G2', 'H2'], 
'H2': ['G1', 'G2', 'G3', 'H1', 'H3'], 
'H3': ['G2', 'G3', 'G4', 'H2', 'H4'], 
'H4': ['G3', 'G4', 'G5', 'H3', 'H5'], 
'H5': ['G4', 'G5', 'G6', 'H4', 'H6'], 
'H6': ['G5', 'G6', 'G7', 'H5'], 
'H7': ['G6', 'G7', 'G8', 'H8'], 
'H8': ['G7', 'G8', 'G9', 'H7', 'H9'], 
'H9': ['G8', 'G9', 'H8']
}


# Implementation of the steepest-ascent Hill Climbing algorithm.

# Our final list that we will return.
visited = []

# steep(root, goal)                      
# root: The node that we start at.
# goal: The node that we are trying to get to.
def steep(root, goal):
	
	# Queue of child nodes that will be searched on.
	queue = []

	# In my implementation, my heuristic is described as:
	# - If the node that you are searching has children (in other words, you can walk there)...
	# - Find the child that has the most children of its own (the most possible directions to go).
	# - Go to that node and perform the search again.
	# - Keep going until you either find the goal, or get stuck.

	# A way to keep track of the node with the most children.
	biggest_count = 0
	# The node with the most children.
	big_key = 'a'
	
	# Add the node that we are currently on to the visited list.
	if (root not in visited):
		visited.append(root)

	# If the node that we are on is the goal...
	if (root == goal):
		# We have successfully navigated the map
		visited.append(root)
		print("Success")
		print("Nodes visited:")
		return visited
	
	# Look at what nodes we haven't visited yet...
	for ele in map_graph[root]:
		if (ele not in visited):
			# and add them to the queue.
			queue.append(ele)
	
	# debug
	# print("queue: " + str(queue))
	# print("visited: " + str(visited))

	# Check all items in the queue
	for key in queue:
		# The child count of the node in the queue we are checking.
		count = 0
		# Check all children of the node in the queue.
		for ele in map_graph[key]:
			count += 1
		# Keep track of node with the most children so far.
		if (count > biggest_count):
			biggest_count = count
			big_key = key
	
	# If the node we are on has children...
	if (biggest_count > 0):
		# Recursively check the next node.
		return steep(big_key, goal)
	
	# Otherwise, we have found the goal.
	elif (big_key == goal):
		print("Success")
		print("Nodes visited:")
		return visited
	
	# Failure condition. We have gotten stuck somewhere.
	print("Failure")
	print("Nodes visited:")
	return visited

# In this example, we are trying to traverse from A1 (key 0) to H9 (key 71).
# We technically could start from anywhere and try to get to anywhere in the map.
# We could try different examples and see if the algorithm is successful.
print(steep(list(map_graph.keys())[0], list(map_graph.keys())[71]))
