def f(s):
    n = 4
    while s < 37:
        s += 3
        n *= 2
    return n

for x in range(1, 1<<20):
    if f(x) == 128:
        break

print(x)
