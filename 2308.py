a = [x for x in range(3394, 8599) if x % 3 == 1]
a = [x for x in a if x % 7 == 5]
print(max(a), sum(a))