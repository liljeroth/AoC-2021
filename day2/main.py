#!/usr/bin/python3

# Read input file
day_file = open('input','r')
c = day_file.read().split('\n')[:-1]

# Solve part 1
position = 0
depth = 0
for i in range(0, len(c)):
	direction = c[i].split(' ')[0]
	steps = int(c[i].split(' ')[1])
	
	if direction == 'forward':
		position += steps
	elif direction == 'down':
		depth += steps
	elif direction == 'up':
		depth -= steps

print('Answer part 1: ', position*depth)

# Solve part 2
position = 0
depth = 0
aim = 0
for i in range(0, len(c)):
	direction = c[i].split(' ')[0]
	steps = int(c[i].split(' ')[1])
	
	if direction == 'forward':
		position += steps
		depth += aim * steps
	elif direction == 'down':
		aim += steps
	elif direction == 'up':
		aim -= steps

print('Answer part 2: ', position*depth)
