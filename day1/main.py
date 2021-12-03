#!/usr/bin/python3

# Read input file
day_file = open('input','r')
c = day_file.read().split('\n')[:-1]

# Convert to int
d = list(map(int, c))

# Solve part 1
s1 = 0
for i in range(1, len(d)):
	s1 += 1 if d[i] > d[i-1] else 0
 	
print('Answer part 1: ', s1)

# Solve part 2
s2 = 0
for i in range(1, len(c)-2):
	v1 = d[i] + d[i+1] + d[i+2]
	v2 = d[i-1] + d[i] + d[i+1]
	
	s2 += 1 if v1 > v2 else 0
  	
print('Answer part 2: ', s2)
