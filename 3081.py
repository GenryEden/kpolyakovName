from functools import cache

@cache
def f(x):
	if x >= 65:
		return 0
	else:
		cands = [x+1, x+2, x*3]
		vPos = []
		pPos = []
		for xc in cands:
			res = f(xc)
			if res <= 0:
				pPos.append(res)
			else:
				vPos.append(res)
		if pPos:
			return -max(pPos) + 1
		else:
			return -max(vPos)

for x in range(1, 64+1):
	print(x, f(x), sep='\t')
