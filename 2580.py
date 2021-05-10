def getDels(x):
	for i in range(2, x//2+1):
		if x % i == 0:
			yield i

ans = []
maximal = 0

for i in range(586132, 586430+1):
	l = list(getDels(i))
	numOfDels = len(l) + 2
	if numOfDels > maximal:
		maximal = numOfDels
		ans = [[numOfDels, l[-1]]]
	elif numOfDels == maximal:
		ans.append([numOfDels, l[-1]])

print(*ans[0])	
print(*ans[-1])	