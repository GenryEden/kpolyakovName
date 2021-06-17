from functools import cache

@cache
def f(x, y):
	if x + y >= 73:
		return 0
	else:
		cands = [[x+2, y], [x, y+2], [x*2, y], [x, y*2]]
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

for s in range(1, 63+1):
	print(s, f(9, s), sep='\t')

