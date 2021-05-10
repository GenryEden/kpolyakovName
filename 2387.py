limit = 45
dp = [[None for _ in range(limit*3 + 1)] for _ in range(limit*3 + 1)]
for x in range(limit*3, 0, -1):
	for y in range(limit*3, 0, -1):
		if x + y >= limit:
			dp[x][y] = 0
			dp[y][x] = 0
		else:
			cands = [[x+1, y], [x, y+1], [x*3, y], [x, y*3]]
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

file = open('2387.csv', 'w')

print('', *range(1, limit*3 + 1), file=file, sep=';')
for i, x in enumerate(dp):
	if i == 0:
		continue
	print(i, *x[1:], file=file, sep=';')

file.close()