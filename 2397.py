from functools import cache

@cache
def f(x, y):
	if x + y >= 75:
		return 0
	else:
		cands = [[x+1, y], [x, y+1], [x*2, y], [x, y*2]]
		vPos = []
		pPos = []
		for xc, yc in cands:
			res = f(xc, yc)
			if res <= 0:
				pPos.append(res)
			else:
				vPos.append(res)
		if pPos:
			return -max(pPos) + 1
		else:
			return -max(vPos)

for s in range(1, 69+1):
	print(s, f(5, s), sep='\t')