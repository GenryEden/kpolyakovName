for x in range(5, 1<<20):
	res = int('13', x)*int('31', x) 
	if res == int('423', x):
		break

print(x)