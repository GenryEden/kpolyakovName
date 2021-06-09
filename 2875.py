from functools import cache

@cache
def getSimpleDels(x):
	i = 2
	if x == 1:
		return set()
	while x % i != 0:
		i += 1
	ans = getSimpleDels(x//i).copy()
	ans.add(i)
	return ans

cnt = 0

for i in range(2, 20000):
	if len(getSimpleDels(i)) > 3:
		cnt += 1

print(cnt)