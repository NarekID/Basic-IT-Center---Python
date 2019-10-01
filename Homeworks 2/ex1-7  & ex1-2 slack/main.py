import random
def check_ex(func_name, arg, ret):
    if ret == func_name(arg):
        return True
    return False
def random_array(n=5, a=0, b=9):
    arr = []
    for i in range(n):
        arr.append(random.randint(a, b))
    return arr
def ex1(n=5):
    if n != 0:
        n += ex1(n - 1)
    return n
def ex2(s):
    s = str(s)
    if len(s) == 0:
        return
    print(s[0])
    ex2(s[1:])
def ex3(file):
    f = open(file, "r")
    rows = f.readlines()
    row1 = rows[0].split(",")
    row2 = rows[1].split(",")
    max1 = int(row1[0])
    min1 = int(row2[0])
    for i in row1:
        if max1 < int(i):
            max1 = int(i)
    for i in row2:
        if min1 > int(i):
            min1 = int(i)
    f.close()
    return max1 * min1
def ex4(file):
    f = open(file, "r")
    rows = f.readlines()
    a = 0
    z = 0
    n = 0
    for i in range(len(rows)):
        for j in rows[i]:
            if i is 0:
                if 'a' in j:
                    a += 1
            elif i is 1:
                if 'z' in j:
                    z += 1
            else:
                if j.isdigit():
                    n += 1
    f.close()
    print("a = ", a)
    print("z = ", z)
    print("num = ", n)
def ex5(arr, file):
    n = len(arr)
    if n == 0:
        return
    f = open(file, "w") #r+ w w+
    s = 0
    for i in arr:
        s += i
    f.write(str(s))
    f.close()
    print("Done! Check ", file, " file!")
def ex6(file):
    f = open(file, "r")
    rows = f.readlines()
    c = 0
    for i in rows:
        if len(i) > 10:
            c += 1
    f.close()
    return c
def ex7(file):
    f = open(file, "r")
    arr = f.readline().split(",")
    n = len(arr)
    if n == 0 or n == 1:
        f.close()
        return "Empty file!"
    sum1 = 0
    c = 0
    for i in range(1, n, 2):
        sum1 += int(arr[i])
        c += 1
    f.close()
    if c is 0:
        return 0
    else:
        return sum1 / c
def ex1a(n):
   for i in range(2, n // 2 + 1):
       if n % i is 0:
           return False
   return True
def ex2a(n):
    if type(n) is int:
        n = str(n)
        mul1 = 1
        for i in n:
            mul1 *= int(i)
        return mul1
    else:
        return 0
my_arr = [1, 2, 3, 4, 5]
# rand_arr = random_array(5, 0, 9)
# print(check_ex(ex1, 5, 15))
# n = len(my_arr)
# for i in range(100):      # tpel parz tvery
#     if check_ex(ex1a, i, True):
#         print(i, end=" ")
# print()
print(check_ex(ex2a, 4231, 24))