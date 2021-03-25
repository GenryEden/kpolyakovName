n = int(input())
arr = sorted([int(input()) for _ in range(n)])
available = sum(arr)*0.9
for x in range(n):
	s = sum(arr[:x]) + sum(arr[x:])*0.8
	if s > available:
		break
print(x-1)
delta = available - (s - arr[x-2]) 
for i in range(x-2, n):
	if arr[i]*0.2 > delta:
		break
print(arr[i])