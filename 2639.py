n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()
arr = arr[k:-k]
print(arr[-1], sum(arr)/len(arr))