n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()
ans = 0
for step in range(1, 100+1):
	lengths = []
	for i in range(0, n):
		try:
			k = i - 1
			while k >= 0 and arr[i] - arr[k] < step:
				k -= 1
			if arr[i] - arr[k] == step:
				lengths.append(lengths[k]+1)
			else:
				raise ValueError
		except ValueError:
			lengths.append(1)
	# print(max(lengths), lengths)
	ans = max(ans, max(lengths))

print(ans)