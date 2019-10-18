arr = [1, 4, 2, -24, -43, 0, -100, 23, 45, 12, -5, 4]

ex281 = list(filter(lambda n: n > 0, arr))
print("ex281", ex281)

ex282 = list(filter(lambda n: n != 0, arr))
print("ex282", ex282)

ex283 = list(filter(lambda n: n % 2 == 1, arr))
print("ex283", ex283)

a = 0
b = 9
ex284 = list(filter(lambda n: a <= n <= b, arr))
print('ex284', ex284)

p = 3
ex285 = list(filter(lambda n: n % p == 0, arr))
print("ex285", ex285)

ex286 = list(filter(lambda n: n % 2 == 0, arr))
print('ex286', ex286)

c = 10
d = 20
ex289 = list(filter(lambda n: c < n * n < d, arr))
print('ex286', ex289)

ex290 = list(filter(lambda n: n % 6 == 1, arr))
print('ex286', ex290)