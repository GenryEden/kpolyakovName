from functools import lru_cache

@lru_cache
def f(n):
    if n <= 3:
        return n
    elif n % 2 == 0:
        return n + 3 + f(n-1)
    else:
        return n*n + f(n-2)
cnt = 0
for x in range(1, 1000+1):
    res = f(x)
    if res % 7 == 0:
        cnt += 1
print(cnt)
