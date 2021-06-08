limit = 69
dp = [[None for _ in range(limit*2+2+1)] for _ in range(limit*2+2+1)]

for x in range(limit*2 + 2, 0, -1):
	for y in range(limit*2 + 2, 0, -1):
		if x + y >= limit:
			dp[x][y] = 0
		else:
			cands = [[x+2, y], [x, y+2], [x*2, y], [x, y*2]]
			allPos = []
			notPosPos = []
			for xc, yc in cands:
				res = dp[xc][yc]
				if res <= 0:
					notPosPos.append(res)
				allPos.append(res)
			if notPosPos:
				dp[x][y] = -max(notPosPos) + 1
			else:
				dp[x][y] = -max(allPos)

file = open('2407.csv', 'w')

print('', *range(1, limit*2+2+1), sep=';', file=file)

for i, x in enumerate(dp):
	if i != 0:
		print(i, *x[1:], sep=';', file=file)

file.close()