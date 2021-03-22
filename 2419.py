limit = 62
dp = [[None for _ in range(limit*2 + 3)] for _ in range(limit*2 + 3)]

for x in range(limit*2 + 2, 0, -1):
	for y in range(limit*2 + 2, 0, -1):
		if x + y >= limit:
			dp[x][y] = 0
		else:
			cands = [[x+3, y],[x, y+3],[x*2, y],[x, y*2]]
			allPos = []
			notPosPos = []
			for xc, yc in cands:
				try:
					res = dp[xc][yc]
					if res <= 0:
						notPosPos.append(res)
					allPos.append(res)
				except (IndexError, TypeError):
					pass
				if notPosPos:
					dp[x][y] = -max(notPosPos) + 1
				elif allPos:
					dp[x][y] = -max(allPos)

file = open('2419.csv', 'w')

print('', *range(1, limit*2 + 3), file=file, sep=';')
for i, x in enumerate(dp):
	if i != 0:
		print(i, *x[1:], file=file, sep=';')

file.close()