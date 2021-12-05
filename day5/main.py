#!/usr/bin/python3

# Read input file
day_file = open('input','r')
c = day_file.read().split('\n')[:-1]

# Find size of grid
size = 0
for r in c:
	x1 = int(r.split(',')[0])
	y1 = int(r.split('->')[0].split(',')[1])
	
	x2 = int(r.split('->')[1].split(',')[0])
	y2 = int(r.split(',')[2])
	
	if max(x1, x2, y1, y2) > size:
		size = max(x1, x2, y1, y2)

# Set zero-grid
grid = []
grid_row = [0] * (size + 1)

for i in range(0, (size + 1)):
	grid.append(grid_row.copy())

# Solve part 1
for r in c:
	x1 = int(r.split(',')[0])
	y1 = int(r.split('->')[0].split(',')[1])
	
	x2 = int(r.split('->')[1].split(',')[0])
	y2 = int(r.split(',')[2])
	
	if x1 == x2:
		for y in range(min(y1, y2), max(y1, y2)+1):
			grid[y][x1] += 1
	
	if y1 == y2:
		for x in range(min(x1, x2), max(x1, x2)+1):
			grid[y1][x] += 1
	

s1 = 0
for row in range(0, len(grid)):
	for col in range(0, len(grid[row])):
		if grid[row][col] >= 2:
			s1 += 1

print('Answer part 1: ', s1)

# Solve part 2
grid = []
grid_row = [0] * (size + 1)

for i in range(0, (size + 1)):
	grid.append(grid_row.copy())

for r in c:
	x1 = int(r.split(',')[0])
	y1 = int(r.split('->')[0].split(',')[1])
	
	x2 = int(r.split('->')[1].split(',')[0])
	y2 = int(r.split(',')[2])
	
	if x1 == x2:
		for y in range(min(y1, y2), max(y1, y2)+1):
			grid[y][x1] += 1
	
	elif y1 == y2:
		for x in range(min(x1, x2), max(x1, x2)+1):
			grid[y1][x] += 1
			
	elif True:
		for i in range(0, abs(x2 - x1) + 1):
		
			xd = i
			if x2 > x1 :
				xd *= -1
				
			yd = i
			if y2 > y1 :
				yd *= -1
				
			grid[y2 + yd][x2 + xd] += 1

s2 = 0
for row in range(0, len(grid)):
	for col in range(0, len(grid[row])):
		if grid[row][col] >= 2:
			s2 += 1

print('Answer part 2: ', s2)

