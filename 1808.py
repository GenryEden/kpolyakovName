def f(s):
	n = 5
	while s > 5:
		s //= 2
		n += 4
	return n

# программа выведет все такие s, найти наибольшее нужно самим

for s in range(1, 1<<20):
	if f(s) == 29:
		print(s)