def primeFactors(x):
	start = x
	divs = []
	d = 2
	while d*d <= x:
		if x % d == 0:
			x //= d
			if d != start:
				divs.append(d)
		else:
			d += 1
	if x != start:
		divs.append(x)
	ans = 0
	for i in set(divs):
		ans += i
	return ans

for x in range(33333, 55555+1):
        res = primeFactors(x)
        if res == 0:
                continue
        if x % res == 0 and res > 250:
                print(x, res)
