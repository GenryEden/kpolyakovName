def toCountSystem(x, y):
    ans = ''
    while x:
        ans += str(x % y)
        x //= y
    return ans[::-1]

print(toCountSystem(9**8 + 3**24 - 6, 3).count('2'))
