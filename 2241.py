def check(A):
    for x in range(1, 18*54+1):
        res = bool(x % 18) or (bool(x % 54) or not(x % A))
        if not res:
            return False
    return True
last = -1
for a in range(1, 1<<20):
    if check(a):
    	last = a

print(last)