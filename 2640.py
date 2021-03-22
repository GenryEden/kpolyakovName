n, k, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()

winners = arr[-k:]
prizers = arr[-k-m:-k]

print(prizers[0], winners[0])