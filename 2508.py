ans = []
maximal = 0
prev = ''
cnt = 1
s = input()
for i in s:
	if i == prev:
		cnt += 1
	else:
		if cnt > maximal:
			maximal = cnt
			ans = [[maximal, prev]]
		elif cnt == maximal:
			ans.append([maximal, prev])
		cnt = 1
	prev = i

if cnt > maximal:
	maximal = cnt
	ans = [[maximal, prev]]
elif cnt == maximal:
	ans.append([maximal, prev])

for x in ans:
	print(*x[::-1])