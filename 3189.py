from functools import cache

@cache
def f(x, y):
	if x + y >= 108:
		return False
	else:
		cands = [[x+1,y], [x,y+1], [x*4,y], [x,y*4]]
		vPos = []
		pPos = []
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

for s in range(1, 101+1):
	print(s, f(s, 6), sep='\t')