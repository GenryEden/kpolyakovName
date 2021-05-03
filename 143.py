def f(x):
	assert 10000 <= x <= 99999
	s = str(x)
	a = int(s[0]) + int(s[2]) + int(s[4])
	b = int(s[1]) + int(s[3])
	if a > b:
		return int(str(b) + str(a))
	else:
		return int(str(a) + str(b))


for x in range(10000, 1<<20):
	if f(x) == 723:
		break

print(x)