import random
def check_ex(func_name, arg, ret):
    if ret == func_name(arg):
        return True
    return False
def rand_array(n = 4, a = -5, b = 5):
    temp_arr = []
    for i in range(n):
        temp_arr.append(random.randint(a,b))
    return temp_arr
def rand_matrix(n = 4, a = -5, b = 5):
    temp_matrix = []
    for i in range(n):
        temp_matrix.append(rand_array(n, a, b))
    return temp_matrix
def ex434(arr):
    n = len(arr)
    sum1 = 0
    for i in range(n):
        for j in range(n - i - 1, n):
            minus = False
            if arr[i][j] < 0:
                arr[i][j] = - arr[i][j]
                minus = True
            if arr[i][j] > 5.4 and arr[i][j] < 15.3:
                if minus:
                    arr[i][j] = -arr[i][j]
                sum1 += arr[i][j]
    return sum1
def ex435(arr):
    n = len(arr)
    c = 0
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[i][j] % 5 is 0:
                c += 1
    return c
def ex436(arr, a = 1, b = 5):
    n = len(arr)
    c = 0
    sum1 = 0
    for i in range(1, n):
        for j in range(i):
            if arr[i][j] > a and arr[i][j] < b:
                sum1 += arr[i][j]
                c += 1
    if c is 0:
        return 0
    else:
        return sum1 / c
def ex437(arr):
    n = len(arr)
    c = 0
    sum1 = 0
    for i in range(n):
        for j in range(i+1):
            if arr[i][j] is int(arr[i][j]):
                sum1 += arr[i][j] ** 2
                c += 1
    if c is 0:
        return 0
    else:
        return (sum1 / c) ** 0.5
def ex438(arr):
    n = len(arr)
    c = 0
    for i in range(1, n):
        for j in range(i):
            if j % 2 is 0 and arr[i][j] > 0:
                c += 1
    return c
def ex439(arr):
    n = len(arr)
    mul1 = 1
    for i in range(n - 1):
        for j in range(i + 1, n):
            if (i + j) % 2 is 1:
                mul1 *= arr[i][j]
    return mul1
def ex440(arr):
    n = len(arr)
    sum1 = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if (i + j) % 2 is 0:
                sum1 += arr[i][j]
    return sum1
def ex441(arr):
    n = len(arr)
    c = 0
    sum1 = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[i][j] > 0:
                sum1 += arr[i][j] ** 2
                c += 1
    if c is 0:
        return 0
    else:
        return (sum1 / c) ** 0.5
def ex442(arr):
    n = len(arr)
    c = 0
    sum1 = 0
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[i][j] < 0:
                sum1 += arr[i][j]
                c += 1
    if c is 0:
        return 0
    else:
        return sum1 / c
def ex443(arr):
    n = len(arr)
    c = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[i][j] is 0:
                c += 1
    return c
def ex444(arr):
    n = len(arr)
    c = 0
    for i in range(1, n - 1, 2):
        for j in range(i + 1, n):
            if arr[i][j] < 0:
                c += 1
    return c
def ex445(arr, k = 5):
    n = len(arr)
    c = 0
    for i in range(1, n):
        for j in range(i):
            if arr[i][j] < 0:
                arr[i][j] = -arr[i][j]
            if arr[i][j] > k:
                c += 1
    return c
def ex446(arr, a = 1, b = 5):
    n = len(arr)
    sum1 = 0
    for i in range(n):
        for j in range(i, n):
            if (arr[i][j] > a) and (arr[i][j] < b):
                sum1 += arr[i][j]
    return sum1
def ex447(arr, a = 5):
    n = len(arr)
    mul1 = 1
    for i in range(n):
        for j in range(n - i - 1, n):
            if arr[i][j] < a:
                mul1 *= arr[i][j]
    return mul1
def ex448(arr):
    n = len(arr)
    sum1 = 0
    c = 0
    for i in range(n):
        for j in range(i, n):
            if (i + j) % 2 is 0:
                sum1 += arr[i][j]
                c += 1
    if c is 0:
        return 0
    else:
        return sum1 / c
def ex449(arr):
    n = len(arr)
    sum1 = 0
    for i in range(n - 1):
        for j in range(n - i - 1):
            if int(arr[i][j]) % 4 is 0:
                sum1 += arr[i][j]
    return sum1
def ex450(arr):
    n = len(arr)
    sum1 = 0
    for i in range(1, n):
        for j in range(n - i, n):
            if arr[i][j] - int(arr[i][j]) > 0:
                sum1 += arr[i][j] - int(arr[i][j])
    return round(sum1, 12)
my_arr = [[5, 10, 4],
          [3, 2.005, 6.00001],
          [2, 12.04, 10.1]]
#rand_arr = rand_matrix(4, -9, 9)
#print(check_ex(ex450, my_arr, 0))
#print(ex450(my_arr))