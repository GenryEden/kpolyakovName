s = input()
prev = ''
d = {}
for i in s:
	if prev == 'X':
		try:
			d[i] += 1
		except KeyError:
			d[i] = 1
	prev = i

maxCnt = 0
ans = ''

for key in d:
	if d[key] > maxCnt:
		maxCnt = d[key]
		ans = key
	elif d[key] == maxCnt:
		if ans > key:
			ans = key

print(ans, maxCnt)