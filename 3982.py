from math import log
ans = []
for m in range(1, 30, 2):
	for n in range(0, 15, 2):
		res = 2**m
		res *= 7**n
		if 100000000 <= res <= 300000000:
			ans.append([res, m+n])
ans.sort()
for i in ans:
	print(*i)