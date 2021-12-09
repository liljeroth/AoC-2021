#!/usr/bin/python3
import statistics

# Read input file
day_file = open('input','r')
c = day_file.read().split('\n')[:-1]

# # Convert to int
#c = list(map(int, c))

# Solve part 1

low_points = []
for i in range(0, len(c)):

	for j in range(0, len(c[i])):
		is_low = True
		
		if i > 0:
			if int(c[i][j]) >= int(c[i-1][j]):
				is_low = False
				
		if i < len(c) - 1:
			if int(c[i][j]) >= int(c[i+1][j]):
				is_low = False
				
		if j > 0:
			if int(c[i][j]) >= int(c[i][j-1]):
				is_low = False
				
		if j < len(c[i]) - 1:
			if int(c[i][j]) >= int(c[i][j+1]):
				is_low = False
		
		if is_low:
			low_points.append([i, j])

s1 = 0
for i in range(0, len(low_points)):
	l = low_points[i]
	s1 += int(c[int(l[0])][int(l[1])]) + 1

print('Answer part 1: ', s1)

# Solve part 2
# 351900 too low

def get_basin(m, i, j, r):
	b = [[i,j]]
	
	if i > 0:

		if int(c[i][j]) == int(c[i-1][j]) - 1 and int(c[i-1][j]) < 9:
			b.append([i-1, j])
			
			if r == True:
				t = get_basin(m, i-1, j, r)
				if len(t) > 1:
					for n in t[1:]:
						if n not in b:
							b.append(n)
	
	if i < len(c) - 1:
	
		if int(c[i][j]) == int(c[i+1][j]) - 1 and int(c[i+1][j]) < 9:
			b.append([i+1, j])
			
			if r == True:
				t = get_basin(m, i+1, j, r)
				if len(t) > 1:
					for n in t[1:]:
						if n not in b:
							b.append(n)
	
	if j > 0:
	
		if int(c[i][j]) == int(c[i][j-1]) - 1 and int(c[i][j-1]) < 9:
			b.append([i, j-1])
			
			if r == True:
				t = get_basin(m, i, j-1, r)
				if len(t) > 1:
					for n in t[1:]:
						if n not in b:
							b.append(n)
	
	if j < len(c[i]) - 1:
	
		if int(c[i][j]) == int(c[i][j+1]) - 1 and int(c[i][j+1]) < 9:
			b.append([i, j+1])
			
			if r == True:
				t = get_basin(m, i, j+1, r)
				if len(t) > 1:
					for n in t[1:]:
						if n not in b:
							b.append(n)
				
	return b

basins = []
lengths = []
for k in range(0, len(low_points)):
	
	i = int(low_points[k][0])
	j = int(low_points[k][1])
	
	b = get_basin(c, i, j, True)
	basins.append(b)
	
	lengths.append(len(b))

s2 = 1
for s in sorted(lengths, reverse=True)[:3]:
	s2 *= s

print('Answer part 2: ', s2)

