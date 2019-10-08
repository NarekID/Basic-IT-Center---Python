from random import randint as rnd

class Vector():
    def __init__(self, arr, n=10):
        self.m_arr = []
        self.m_length = n
        for i in range(self.m_length):
            self.m_arr.append(rnd(-10, 10))

    def print_arr(self):
        print(self.m_arr)

    def ex211(self):
        s = 0
        c = 0
        for i in self.m_arr:
            if i > 0:
                s += i
                c += 1
        return s / c

    def ex212(self):
        s = 0
        c = 0
        for i in self.m_arr:
            if i > 0:
                s += i ** 2
                c += 1
        return (s / c) ** 0.5

    def ex213(self):
        s = 0
        c = 0
        for i in self.m_arr:
            if i < 0:
                s += i ** 2
                c += 1
        return (s / c) ** 0.5

    def ex214(self):
        s = 0
        c = 0
        for i in self.m_arr:
            if i < 0:
                s += i
                c += 1
        return s / c

    def ex215(self):
        s = 0
        for i in range(self.m_length):
            if i % 2 is 0:
                s += self.m_arr[i]
        return s

    def ex216(self):
        m = 1
        for i in range(self.m_length):
            if i % 2 is 0:
                m *= self.m_arr[i]
        return m

    def ex217(self):
        m = 1
        for i in range(self.m_length):
            if i % 2 is 1:
                m *= self.m_arr[i] ** 2
        return m

    def ex218(self):
        s = 0
        for i in range(self.m_length):
            if i % 2 is 1:
                s += abs(self.m_arr[i])
        return s

    def ex219(self, k=2):
        c = 0
        for i in range(self.m_length):
            if i % k is 0:
                c += 1
        return c

    def ex220(self):
        neg = 0
        pos = 0
        for i in self.m_arr:
            if i < 0:
                neg += 1
            if i > 0:
                pos += 1
        return neg, pos

    def ex221(self, a=5, b=15):
        s = 0
        for i in self.m_arr:
            if a <= i <= b:
                s += i
        return s

    def ex222(self, a=5, b=15):
        m = 1
        for i in self.m_arr:
            if a <= i < b:
                m *= i
        return m

    def ex223(self, a=5, b=15):
        c = 0
        for i in self.m_arr:
            if a < i < b:
                c += 1
        return c

    def ex224(self, k=5):
        s = 0
        for i in self.m_arr:
            if abs(i) < k:
                s += i ** 3
        return s

    def ex225(self, t=5):
        m = 1
        for i in self.m_arr:
            if abs(i) < t:
                m *= i
        return m

    def ex226(self, k=5):
        c = 0
        for i in self.m_arr:
            if abs(i) < k:
                c += 1
        return c

    def ex227(self, k=3):
        s = 0
        c = 0
        for i in range(self.m_length):
            if i % k is 0:
                s += self.m_arr[i]
                c += 1
        return s / c

    def ex228(self, k=3):
        s = 0
        for i in range(self.m_length):
            if i % int(k):
                s += i
        return s

    def ex229(self):
        m = 1
        for i in range(self.m_length):
            if self.m_arr[i] - i > 0:
                m *= self.m_arr[i]
        return m

    def ex230(self, k=5):
        s = 0
        c = 0
        for i in self.m_arr:
            if int(i) % int(k) is 0:
                s += i ** 2
                c += 1
        return (s / c) ** 0.5


my_arr = Vector(10)
my_arr.print_arr()
print("ex211 =", my_arr.ex211())
print("ex212 =", my_arr.ex212())
print("ex213 =", my_arr.ex213())
print("ex214 =", my_arr.ex214())
print("ex215 =", my_arr.ex215())
print("ex216 =", my_arr.ex216())
print("ex217 =", my_arr.ex217())
print("ex218 =", my_arr.ex218())
print("ex219 =", my_arr.ex219(3))
print("ex220 =", my_arr.ex220())
print("ex221 =", my_arr.ex221(0, 5))
print("ex222 =", my_arr.ex222())
print("ex223 =", my_arr.ex223())
print("ex224 =", my_arr.ex224(5))
print("ex225 =", my_arr.ex225(5))
print("ex226 =", my_arr.ex226(5))
print("ex227 =", my_arr.ex227(2))
print("ex228 =", my_arr.ex228(3))
print("ex229 =", my_arr.ex229())
print("ex230 =", my_arr.ex230(5))