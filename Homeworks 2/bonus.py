import random
def rand_array(n = 4, a = 0, b = 9):
    temp_arr = []
    for i in range(n):
        temp_arr.append(random.randint(a,b))
    return temp_arr
def rand_matrix(n = 4, a = 0, b = 9):
    temp_matrix = []
    for i in range(n):
        temp_matrix.append(rand_array(n, a, b))
    return temp_matrix
def replace_matrix(arr, k):
    n = len(arr)
    if n is 0 or n is 1 or n is 2:
        return "Min length is 3"
    if n % 2 is 0:
        for i in range(n//2 - 1, n//2 + 1):
            for j in range(n//2 - 1, n//2 + 1):
                arr[i][j] = k
    elif n % 2 is 1:
        arr[n//2][n//2] = k
    return arr
def print_matrix(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end="\t")
        print()
def input_num(message):
    while 1:
        try:
            i = int(input(message))
            return i
        except ValueError:
            print("Enter a number!")
# arr = [[1,2,3],
#        [4,5,6],
#        [7,8,9]]
# n = len(arr)
# arr2 = [[0,1,2,3],
#         [4,5,6,7],
#         [8,9,8,7],
#         [6,5,4,3]]
# n2 = len(arr2)
arr = rand_matrix(20, 0, 9)
print_matrix(arr)
k  = input_num("Enter random number:")
arr = replace_matrix(arr, k)
print_matrix(arr)

