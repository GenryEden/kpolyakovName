from functools import cache

@cache
def f(x, y):
	if x + y >= 90:
		return 0
	else:
		cands = [[x+1, y], [x, y+1], [x*3, y], [x, y*3]]
		pPos = []
		vPos = []
		for xc, yc in cands:
			res = f(xc, yc)
			if res > 0:
				vPos.append(res)
			else:
				pPos.append(res)
		if pPos:
			return -max(pPos) + 1
		else:
			return -max(vPos)

l = [f(9, s) for s in range(1, 80+1)]
print(l.count(2))
print(max([i+1 for i, x in enumerate(l) if x == -2]))