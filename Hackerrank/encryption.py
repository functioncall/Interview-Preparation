import math

string = raw_input().replace(" ","")

f_length = int(math.floor(math.sqrt(len(string)))) # Rows
c_length = int(math.ceil(math.sqrt(len(string))))  # Columns
output = []

def grid_axis(rows,columns):
	# Base case
	if rows*columns >= len(string):
		return rows, columns
	else:
		rows+=1
		grid_axis(rows, columns)

row, col = grid_axis(f_length,c_length)

# Make the grid
grid = [['' for x in range(col)] for x in range(row)]

def encode(r, c):
	index = 0
	for i in xrange(0,r):
		for j in xrange(0,c):
			if index < len(string):
				# Storing string characters in the grid
				grid[i][j] = string[index]
				index+=1
	return

def display(row, col):
	for i in xrange(col):
		for j in xrange(row):
			if j == row-1:
				# print i,j,grid[j][i]
				output.append(grid[j][i])
				output.append(' ')
			else:
				output.append(grid[j][i])
	return output
encode(row, col)
output = display(row, col)

print " ".join(map(str,output))