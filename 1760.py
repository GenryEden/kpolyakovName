def f(x):
	b = bin(x)[2:]
	b = b[::-1]
	return int(b, 2)

# программа найдет все такие х, в ответ - последнее
for x in range(1, 100+1):
	if f(x) == 7:
		print(x)