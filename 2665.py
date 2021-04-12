n = int(input())
dp = [0] + [float('inf')]*4
for _ in range(n):
	newdp = [float('inf')]*5
	a, b = [int(x) for x in input().split()]
	for x in dp:
		if x == float('inf'):
			continue
		for y in a, b:
			res = x + y
			newdp[res%5] = min(newdp[res%5], res)
	dp = newdp[:]
print(dp[0])

