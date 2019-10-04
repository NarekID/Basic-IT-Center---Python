def ex184(n):
    for k in range(int(n ** 0.5), 1, -1):
        if 3 ** k < n:
            return k
    return False
def ex189(n):
    a = 1
    b = 1
    while 1:
        c = a + b
        if c > n:
            return c
        a = b
        b = c
def ex191(x, n):
    s = 0
    for i in range(n + 1):
        s += x ** i
    return s
print(ex184(10))
print(ex189(14))
print(ex191(2, 4))