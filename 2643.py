n = int(input())
arr = []

for _ in range(n):
	arr.append(int(input()))

arr.sort()
print('sorted')
cnt = 0
possible = True
while possible:
	possible = False
	for x in arr:
		if (100 - x) in arr:
			possible = True
			cnt += 1
			arr.remove(x)
			arr.remove(100 - x)
			break

print(cnt)