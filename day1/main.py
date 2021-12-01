#!/usr/bin/python3

# 1: 1638335023 (3m 43s)
# 2: 1638335238 (7m 18s)

# Read input file
path = 'day1_input'
day_file = open(path,'r')
c = day_file.read().split('\n')[:-1]

# Solve part 1
count = 0
for i in range(1, len(c)):
	s1 = int(c[i])
	s2 = int(c[i-1])
	
	count += 1 if s1 > s2 else 0
 	
print('Answer part 1: ', count)

# Solve part 2
count = 0
for i in range(1, len(c)-2):
	s1 = int(c[i]) + int(c[i+1]) + int(c[i+2])
	s2 = int(c[i-1]) + int(c[i]) + int(c[i+1])
	
	count += 1 if s1 > s2 else 0
  	
print('Answer part 2: ', count)
