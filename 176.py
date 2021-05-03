def f(d):
	n = 1
	s = 46
	while s <= 2700:
		s += d
		n += 4
	return n

for x in range(1,1<<20):
	if f(x) == 121:
		break

print(x)