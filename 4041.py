def maxDist(string, let):
	maximal = -1
	minimal = -1
	for i, l in enumerate(string):
		if l == let and minimal == -1:
			minimal = i
		elif l == let:
			maximal = i
	return maximal - minimal

file = open('24-164.txt')
ans = 0
for line in file:
	if line.count('G') < 15:
		for l in set(line):
			ans = max(ans, maxDist(line, l))

print(ans)
