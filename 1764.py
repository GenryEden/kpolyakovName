def f(n):
	b = bin(n)[2:]
	b = b[::-1]
	return int(b, 2)
# программа выведет все такие х, найти наибольшее нужно самим
for x in range(1, 1000+1):
	if f(x) == 23:
		print(x)