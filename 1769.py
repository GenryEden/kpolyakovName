def f(x):
    return int(bin(x)[2:][::-1], 2)

for x in range(1001, 1<<20):
    if f(x) == 29:
        break

print(x)
