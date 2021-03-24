n = int(input())
ans = 0
minDistModNot9 = float('inf')
minDistModNot9Reserve = float('inf')

for _ in range(n):
	a, b, c = sorted([int(x) for x in input().split()])
	ans += a + b
	if c - b % 9 != 0:
		minDistModNot9 = min(minDistModNot9, c - b)
	if c - a % 9 != 0:
		minDistModNot9Reserve = min(minDistModNot9Reserve, c - b)

if ans % 9 == 0:
	if minDistModNot9 != float('inf'):
		print(ans + minDistModNot9)
	elif minDistModNot9Reserve != float('inf'):
		print(ans + minDistModNot9Reserve)
else:
	print(ans)