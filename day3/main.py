#!/usr/bin/python3

# Read input file
day_file = open('input','r')
c = day_file.read().split('\n')[:-1]

# Solve part 1
bit_sum = [0] * len(c[0])
for i in range(0, len(c)):
	for j in range(0, len(c[i])):
		bit_sum[j] += int(c[i][j])

gamma   = ""
epsilon = ""
for i in range(0, len(bit_sum)):
	gamma += '1' if bit_sum[i] >= len(c)/2 else '0'
	epsilon += '0' if bit_sum[i] >= len(c)/2 else '1'

print('Answer part 1: ', int(gamma, 2) * int(epsilon, 2))

# Solve part 2
oxy_rating = c.copy()
for j in range(0, len(oxy_rating[0])):
	bit_sum = 0
	
	for i in range(0, len(oxy_rating)):
		bit_sum += int(oxy_rating[i][j])
	
	common = "0" 
	if bit_sum/len(oxy_rating) >= 0.5:
		common = "1"
	
	oxy_rating2 = oxy_rating.copy()
	for o in oxy_rating2:
		if o[j] != common:
			oxy_rating.remove(o)
			
	if len(oxy_rating) == 1:
		break

co2_rating = c.copy()
for j in range(0, len(co2_rating[0])):
	bit_sum = 0
	
	for i in range(0, len(co2_rating)):
		bit_sum += int(co2_rating[i][j])
	
	common = "1" 
	if bit_sum/len(co2_rating) >= 0.5:
		common = "0"
		
	co2_rating2 = co2_rating.copy()
	for o in co2_rating2:
		if o[j] != common:
			co2_rating.remove(o)
			
	if len(co2_rating) == 1:
		break
		
print('Answer part 2: ', int(oxy_rating[0], 2)*int(co2_rating[0], 2))
