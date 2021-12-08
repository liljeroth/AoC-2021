#!/usr/bin/python3
import statistics

# Read input file
day_file = open('input','r')
c = day_file.read().split('\n')[:-1]

s1 = 0
for i in range(0, len(c)):
	for w in c[i].split('|')[1][1:].split(' '):
		l = len(w)
		
		#1
		if l == 2:
			s1 += 1
		#4
		if l == 4:
			s1 += 1
		#7
		if l == 3:
			s1 += 1
		#8
		if l == 7:
			s1 += 1

print('Answer part 1: ', s1)

# Solve part 2
s2 = 0
for i in range(0, len(c)):
	
	m = [''] * 10
	word_sum = '0'
	
	for w in c[i].split('|')[0].split(' '):
		
		if len(w) == 2:
			m[1] = w
		if len(w) == 4:
			m[4] = w
		if len(w) == 3:
			m[7] = w
		if len(w) == 7:
			m[8] = w
			
	for w in c[i].split('|')[0].split(' '):
	
		if len(w) == 5:
			t = m[4].replace(m[1][0], '').replace(m[1][1], '')
			
			if m[1][0] in w and m[1][1] in w:
				m[3] = w
			elif t[0] in w and t[1] in w:
				m[5] = w
			else:
				m[2] = w
				
		if len(w) == 6:
			if not (m[1][0] in w and m[1][1] in w):
				m[6] = w
			elif m[4][0] in w and m[4][1] in w and m[4][2] in w and m[4][3] in w:
				m[9] = w
			else:
				m[0] = w
	
	for w in c[i].split('|')[1][1:].split(' '):
		
		l = len(w)
		
		if l == 2:
			word_sum += '1'
		elif l == 4:
			word_sum += '4'
		elif l == 3:
			word_sum += '7'
		elif l == 7:
			word_sum += '8'
		
		else:
			pos = '023569'
			
			if l == 5:
				pos = pos.replace('0', '')
				pos = pos.replace('6', '')
				pos = pos.replace('9', '')
				
			elif l == 6:
				pos = pos.replace('2', '')
				pos = pos.replace('3', '')
				pos = pos.replace('5', '')
				
			for ch in w:
				for k in range(0, len(m)):
					if not ch in m[k]:
						pos = pos.replace(str(k), '')
			
			word_sum += pos
			
	s2 += int(word_sum)

print('Answer part 2: ', s2)

