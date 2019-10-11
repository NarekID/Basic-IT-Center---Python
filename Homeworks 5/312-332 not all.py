from random import randint as rnd


class Vector():
    count = 0

    def __init__(self, n):
        Vector.count += 1
        self.__arr = []
        self.__length = n
        for i in range(self.__length):
            self.__arr.append(rnd(-10, 10))

    def set_arr(self, arr):
        self.__arr = arr

    def get_arr(self):
        return self.__arr

    @staticmethod
    def arr_count():
        return Vector.count


class Solution():
    def __init__(self, arr):
        self.__arr = arr
        self.__length = len(arr)

    def ex312(self):
        temp = []
        i = 0
        n = self.__length - 1
        while i < n or i == n:
            if abs(self.__arr[i]) >= abs(self.__arr[n]):
                temp.append(self.__arr[i])
            else:
                temp.append(self.__arr[n])
            i += 1
            n -= 1
        return temp

    def ex314(self):
        temp = []
        for i in range(self.__length):
            temp.append(self.__arr[i])
            if self.__arr[i] > 0:
                temp.append(0)
        return temp

    def ex316(self):
        temp = []
        avg = (min(self.__arr) + max(self.__arr)) / 2
        for i in range(self.__length):
            if abs(self.__arr[i]) < avg:
                temp.append(self.__arr[i])
        return temp

    def ex320(self):
        temp = []
        min1 = min(self.__arr)
        max1 = max(self.__arr)
        for i in range(self.__length):
            if self.__arr[i] == min1:
                i_min = i
                break
        for i in range(self.__length - 1, -1, -1):
            if self.__arr[i] == max1:
                i_max = i
                break
        for i in range(self.__length):
            if i == i_min or i == i_max:
                continue
            temp.append(self.__arr[i])
        return temp

    def ex322(self):
        temp = []
        for i in range(self.__length):
            temp.append(self.__arr[i])
            if self.__arr[i] == 0:
                temp.append(0)
                temp.append(0)
        return temp

    def ex323(self):
        temp = []
        avg = (min(self.__arr) + max(self.__arr) / 2)
        for i in range(self.__length):
            if self.__arr[i] > avg:
                temp.append(self.__arr[i])
        return temp

    def ex325(self):
        temp = self.__arr.copy()
        max1 = max(temp)
        for i in range(self.__length):
            if temp[i] == max1:
                i_max = i
                break
        temp[0], temp[i_max] = temp[i_max], temp[0]
        return temp

    def ex326(self):
        temp = self.__arr.copy()
        i = 0
        n = self.__length - 1
        while i < n or i == n:
            temp[i], temp[n] = temp[n], temp[i]
            i += 1
            n -= 1
        return temp

    def ex327(self):
        temp = []
        min1 = min(self.__arr)
        for i in range(self.__length):
            if self.__arr[i] == min1:
                temp.append(i)
            else:
                temp.append(self.__arr[i])
        return temp

    def ex329(self):
        temp = []
        temp2 = 0
        for i in range(self.__length):
            temp2 += self.__arr[i]
            temp.append(temp2)
        return temp

    def ex330(self):
        temp = []
        for i in range(0, self.__length, 2):
            temp.append(int(self.__arr[i]))
        for i in range(1, self.__length, 2):
            temp.append(int(self.__arr[i]))
        return temp

    def ex332(self):
        temp = []
        min1 = min(self.__arr)
        max1 = max(self.__arr)
        for i in range(self.__length):
            if self.__arr[i] == min1:
                temp.append(max1 ** 3)
            elif self.__arr[i] == max1:
                temp.append(min1 ** 2)
            else:
                temp.append(self.__arr[i])
        return temp

a = Vector(10)
arr = a.get_arr()
print(arr)
ex_checker = Solution(arr)
print(ex_checker.ex312())
print(ex_checker.ex314())
print(ex_checker.ex316())
print(ex_checker.ex320())
print(ex_checker.ex322())
print(ex_checker.ex325())
print(ex_checker.ex326())
print(ex_checker.ex327())
print(ex_checker.ex329())
print(ex_checker.ex330())
print(ex_checker.ex332())