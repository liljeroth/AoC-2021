#!/usr/bin/python3

# Read input file
day_file = open('input','r')
c = day_file.read().split('\n')[:-1]

# Solve part 1
d = list(map(int, c[0].split(',')))

for t in range(0, 80):
	for i in range(0, len(d)):
		d[i] -= 1
		if d[i] == -1:
			d[i] = 6
			d.append(8)

s1 = len(d)
print('Answer part 1: ', s1)

# Solve part 2
d = list(map(int, c[0].split(',')))

counts = [0] * 9
for t in d:
	counts[t] += 1

new_counts = counts.copy()
for t in range(0, 256):
	for i in range(1, len(counts)):
		new_counts[i - 1] = counts[i]

	new_counts[len(counts) - 1] = counts[0]
	new_counts[len(counts) - 3] += counts[0]
		
	counts = new_counts.copy()

s2 = 0
for t in counts:
	s2 += t

print('Answer part 2: ', s2)

