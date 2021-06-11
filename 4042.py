def findDistance(s, l):
	first = -1
	last = -1
	for i, x in enumerate(s):
		if x == l and first == -1:
			first = i
		elif x == l:
			last = i
	return last - first

file = open('24-164.txt')
ans = 0
for line in file:
	if line.count('E') < 20:
		for l in set(line):
			ans = max(ans, findDistance(line, l))
			
print(ans)	