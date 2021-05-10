def f(x):
	q = 9
	l = 0
	while x >= q:
		l += 1
		x -= q
	m = x
	if m < l:
		m = l
		l = x
	return l, m

# программа находит все такие значения, в ответ пишем последнее

for i in range(1, 1<<10):
	res = f(i)
	if res[0] == 4 and res[1] == 5:
		print(i)