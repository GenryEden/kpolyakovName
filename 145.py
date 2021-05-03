def f(x):
	assert 100 <= x <= 999
	s = str(x)
	a = int(s[0])*int(s[1])
	b = int(s[2])*int(s[1])
	if a > b:
		return int(str(b) + str(a))
	else:
		return int(str(a) + str(b))


ans = 0
for x in range(100, 1000):
	if f(x) == 621:
		ans = x

print(ans)