#!/usr/bin/python3

# Read input file
day_file = open('input','r')
c = day_file.read().split('\n')[:-1]

def isBingo(b):

	for j in range(0, 5):
	
		if b[j] == 'x x x x x':
			return True
		
		if b[0].split(' ')[j] == 'x' and b[1].split(' ')[j] == 'x' and b[2].split(' ')[j] == 'x' and b[3].split(' ')[j] == 'x' and b[4].split(' ')[j] == 'x':
			return True
			
	if b[0].split(' ')[0] == 'x' and b[1].split(' ')[1] == 'x' and b[2].split(' ')[2] == 'x' and b[3].split(' ')[3] == 'x' and b[4].split(' ')[4] == 'x':
		return True
		
	if b[4].split(' ')[0] == 'x' and b[3].split(' ')[1] == 'x' and b[2].split(' ')[2] == 'x' and b[1].split(' ')[3] == 'x' and b[0].split(' ')[4] == 'x':
		return True
	
	return False

# Solve part 1
numbers = c[0].split(',')

min_bingo = len(numbers)
ind_bingo = 0
grd_bingo = []
for i in range(2, len(c), 6):
	grid = []
	
	for j in range(0, 5):
		grid.append(c[i+j])
		grid[j] = grid[j].replace('  ', ' ')
		grid[j] = grid[j].strip()
		
	for n in range(0, len(numbers)):
		
		if n > min_bingo:
			break
			
		for j in range(0, 5):
			grid[j] = (' ' + grid[j] + ' ')
			grid[j] = grid[j].replace(' ' + numbers[n] + ' ', ' x ')
			
		for j in range(0, 5):
			grid[j] = grid[j].replace('xx', 'x')
			grid[j] = grid[j].replace('  ', ' ')
			grid[j] = grid[j].strip()
		
		if isBingo(grid):
			min_bingo = n
			ind_bingo = i
			grd_bingo = grid


s1 = 0
for i in range(0, 5):
	for col in grd_bingo[i].split(' '):
		n = int(col.replace('x', '0'))
		s1 += n

print('Answer part 1: ', s1*int(numbers[min_bingo]))

# Solve part 2
numbers = c[0].split(',')

grd_wins = []
grd_at_win = []
n_at_win = []

for i in range(2, len(c), 6):
	grid = []
	
	for j in range(0, 5):
		grid.append(c[i+j])
		grid[j] = grid[j].replace('  ', ' ')
		grid[j] = grid[j].strip()
		
	for n in range(0, len(numbers)):
	
		if i in grd_wins:
			break
			
		for j in range(0, 5):
			grid[j] = (' ' + grid[j] + ' ')
			grid[j] = grid[j].replace(' ' + numbers[n] + ' ', ' x ')
			
		for j in range(0, 5):
			grid[j] = grid[j].replace('xx', 'x')
			grid[j] = grid[j].replace('  ', ' ')
			grid[j] = grid[j].strip()
		
		if isBingo(grid):
			grd_wins.append(i)
			grd_at_win.append(grid)
			n_at_win.append(n)

max_n = 0
max_n_ind = 0
for i in range(0, len(n_at_win)):
	if n_at_win[i] > max_n:
		max_n = n_at_win[i]
		max_n_ind = i

grd_bingo = grd_at_win[max_n_ind]

s2 = 0
for i in range(0, 5):
	for col in grd_bingo[i].split(' '):
		n = int(col.replace('x', '0'))
		s2 += n

print('Answer part 2: ', s2*int(numbers[max_n]))

