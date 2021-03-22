def f(s):
	n = 0
	while s < s*s:
		s -= 1
		n += 3
	return n

for x in range(1, 1<<20):
	if f(x) > 2000:
		break

print(x)