s = input()

minimal = float('inf')
parse = ''

for l in s:
	if l in '0123456789':
		parse += l
	else:
		if parse:
			res = int(parse)
			if res % 2 == 0:
				minimal = min(minimal, res)
		parse = ''
if parse:
	res = int(parse)
	if res % 2 == 0:
		minimal = min(minimal, res)
print(minimal)