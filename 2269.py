from functools import lru_cache

@lru_cache
def f(n):
    if n <= 3:
        return n
    elif n % 2 == 0:
        return f(n-1) + 2*f(n/2)
    else:
        return f(n-1) + f(n-3)
cnt = 0
for x in range(1, 1<<15):
    try:
        if f(x) < 10**8:
            cnt += 1
    except RecursionError: # функция от некоторых чисел улетает в бесконечность
        pass
print(cnt)
