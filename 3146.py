from itertools import permutations

n = int(input())
dp = [[0, float('-inf')], [float('-inf'), float('-inf')]]

for _ in range(n):
	a, b, c = map(int, input().split())
	newDp = [[float('-inf'), float('-inf')], [float('-inf'), float('-inf')]]
	for combs in permutations([a, b, c]):
		ac, bc, cc = combs
		for firstMod in range(2):
			for secMod in range(2):
				newDp[(firstMod+ac)%2][(secMod+bc)%2] = max(dp[firstMod][secMod] + cc, newDp[(firstMod+ac)%2][(secMod+bc)%2])
	dp = newDp


print(dp[1][0])				
