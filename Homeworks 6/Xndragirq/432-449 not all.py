from random import randint as rnd


class Matrix():
    count = 0

    def __init__(self, n):
        Matrix.count += 1
        self.m_length = n
        self.m_matrix = []
        for i in range(self.m_length):
            self.m_temp_arr = []
            for j in range(self.m_length):
                self.m_temp_arr.append(rnd(-9, 9))
            self.m_matrix.append(self.m_temp_arr)

    def print_matrix(self):
        for i in range(self.m_length):
            for j in range(self.m_length):
                print(self.m_matrix[i][j], end="\t")
            print()

    @staticmethod
    def matrix_count():
        return Matrix.count


class Solution(Matrix):
    def __init__(self, n):
        super().__init__(n)

    def ex432(self):
        s = 0
        c = 0
        for i in range(self.m_length):
            for j in range(self.m_length - i):
                if (i + j) % 2 == 1:
                    s += self.m_matrix[i][j] ** 2
                    c += 1
        if c == 0:
            return c
        else:
            return (s / c) ** 0.5

    def ex435(self):
        c = 0
        for i in range(self.m_length - 1):
            for j in range(self.m_length - i - 1):
                if int(self.m_matrix[i][j]) % 5 == 0:
                    c += 1
        return c

    def ex436(self, a = 0, b = 5):
        s = 0
        c = 0
        for i in range(1, self.m_length):
            for j in range(i):
                if a <= self.m_matrix[i][j] <= b:
                    s += self.m_matrix[i][j]
                    c += 1
        if c == 0:
            return c
        else:
            return s / c

    def ex439(self):
        m = 1
        for i in range(self.m_length - 1):
            for j in range(i + 1, self.m_length):
                if (i + j) % 2 == 1:
                    m *= self.m_matrix[i][j]
        return m

    def ex440(self):
        s = 0
        for i in range(self.m_length - 1):
            for j in range(i + 1, self.m_length):
                if (i + j) % 2 == 0:
                    s += self.m_matrix[i][j]
        return s

    def ex442(self):
        s = 0
        c = 0
        for i in range(self.m_length - 1):
            for j in range(self.m_length - i - 1):
                if self.m_matrix[i][j] < 0:
                    s += self.m_matrix[i][j]
                    c += 1
        if c == 0:
            return c
        else:
            return s / c

    def ex445(self, k = 3):
        c = 0
        for i in range(1, self.m_length):
            for j in range(i):
                if abs(self.m_matrix[i][j]) > k:
                    c += 1
        return c

    def ex447(self, a = 5):
        m = 1
        for i in range(self.m_length):
            for j in range(self.m_length - i - 1, self.m_length):
                if self.m_matrix[i][j] < a:
                    m *= self.m_matrix[i][j]
        return m

    def ex449(self):
        s = 0
        for i in range(self.m_length - 1):
            for j in range(self.m_length - i - 1):
                if int(self.m_matrix[i][j]) % 4 == 0:
                    s += self.m_matrix[i][j]
        return s
my_matrix = Solution(4)
my_matrix.print_matrix()
print()
print("ex432", my_matrix.ex432())
print("ex435", my_matrix.ex435())
print("ex436", my_matrix.ex436(0, 5))
print("ex439", my_matrix.ex439())
print("ex440", my_matrix.ex440())
print("ex442", my_matrix.ex442())
print("ex445", my_matrix.ex445(3))
print("ex447", my_matrix.ex447(5))
print("ex449", my_matrix.ex449())