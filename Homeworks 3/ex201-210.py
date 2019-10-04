def check_ex(ex_num, arg, ret):
    if ret == ex_num(arg):
        return True
    else:
        return False
def ex201(n):
    c = 0
    while n > 0:
        n //= 10
        c += 1
    return c
def ex202(n):
    s = 0
    while n > 0:
        a = n % 10
        s += a
        n //= 10
    return s
def ex203(n):
    m = 1
    while n > 0:
        a = n % 10
        m *= a
        n //= 10
    return m
def ex204(n):
    print("ex204", end=" ")
    while n > 0:
        print(n % 10, end=" ")
        n //= 10
    print()
def ex206(n):
    s = 0
    while n > 0:
        a = n % 10
        s *= 10
        s += a
        n //= 10
    return s
def ex205(n):
    print("ex205", end=" ")
    temp = ex206(n)
    while temp > 0:
        print(temp % 10, end=" ")
        temp //= 10
    print()
def ex207(n):
    while n > 0:
        a = n % 10
        if a is 2:
            return True
        n //= 10
    return False
def ex208(n):
    temp = -1
    while n > 0:
        a = n % 10
        if temp is -1:
            temp = a
        if temp != a:
            return False
        n //= 10
    return True
def ex209(n):
    while n > 0:
        a = n % 10
        if a % 2 is 1:
            return True
        n //= 10
    return False
def ex210(n):
    s1 = 0
    s2 = 0
    c = 0
    while n > 0:
        a = n % 10
        c += 1
        if c % 2 is 0:
            s2 += a
        else:
            s1 += a
        n //= 10
    if s1 == s2:
        return True
    else:
        return False
print("ex201", check_ex(ex201, 1234, 4))
print("ex202", check_ex(ex202, 1001, 2))
print("ex203", check_ex(ex203, 1234, 24))
ex204(4096)
ex205(4096)
print("ex206", check_ex(ex206, 1122, 2211))
print("ex207", check_ex(ex207, 1024, True))
print("ex208", check_ex(ex208, 222, True))
print("ex209", check_ex(ex209, 1344, True))
print("ex210", check_ex(ex210, 1023, True))




