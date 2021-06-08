def getSimpleDels(x):
	X = x
	i = 2
	ans = set()
	while i <= x:
		if x % i == 0 and i != X:
			x //= i
			ans.add(i)
		else:
			i += 1
	return ans

for i in range(25317, 51237+1):
	simpleDels = getSimpleDels(i)
	if len(simpleDels) >= 6:
		print(i, max(simpleDels))