n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()
sale = arr[-k:]
arr = arr[:-k]
print(arr[-1], sum(sale)*0.2)