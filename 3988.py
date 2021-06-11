dp = [[0, float('-inf')], [float('-inf'), float('-inf')]]
n = int(input())
for _ in range(n):
	a, b = map(int, input().split())
	if b % 2 == 0:
		continue
	a, b = sorted([a,b])
	newDp = [dp[0][:], dp[1][:]]
	for mod1 in range(2):
		for mod2 in range(2):
			if dp[mod1][mod2] != float('-inf'):
				if newDp[(mod1+a)%2][(mod2+b)%2] < dp[mod1][mod2] + a + b:
					# print('-'*10)
					# print(dp)
					# print((mod1+a)%2, (mod2+b)%2, mod1, mod2, a, b)
					newDp[(mod1+a)%2][(mod2+b)%2] = dp[mod1][mod2] + a + b
					# print(newDp)
					# print('-'*10)


	dp = newDp

print(dp[1][0])