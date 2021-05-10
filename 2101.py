from random import shuffle

def generate():
	s = list('1'*23 + '2'*5)
	shuffle(s)
	return ''.join(s)

def func(s):
	while '11' in s:
		if '112' in s:
			s = s.replace('112', '5', 1)
		else:
			s = s.replace('11', '3', 1)
	return s

maximal = 0

# перебор будет бесконечным, в ответ писать последнее значение

while True:
	s = func(generate())
	cnt = sum([int(x) for x in s])
	if cnt > maximal:
		print(cnt)
		maximal = cnt
		