#!/usr/bin/python3
import statistics

# Read input file
day_file = open('input','r')
c = day_file.read().split('\n')[:-1]

# # Convert to int
# d = list(map(int, c))

# Solve part 1
d = list(map(int, c[0].split(',')))

center_line = round(statistics.median(d))

s1 = 0
for i in range(0, len(d)):
	s1 += abs(d[i] - center_line)

print('Answer part 1: ', s1)

# Solve part 2
center_line = round(statistics.mean(d))
print(center_line)

lowest_cost = 10000000000
inc_count = 0
prev_cost = 0
for j in range(0, max(d) - 1):
	cost = 0
	
	for i in range(0, len(d)):
		cost += sum(range(0, abs(d[i] - j) + 1))
	
	if cost > prev_cost:
		inc_count += 1
	else:
		inc_count = 0
		
	prev_cost = cost
	
	if inc_count > 5:
		break
	
	if cost < lowest_cost:
		lowest_cost = cost
		
print(lowest_cost)


s2 = 0
for i in range(0, len(d)):
	for k in range(0, abs(d[i] - center_line)):
		s2 += k + 1

print('Answer part 2: ', s2)

