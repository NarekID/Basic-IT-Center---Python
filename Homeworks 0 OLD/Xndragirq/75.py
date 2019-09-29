import math
x = -math.pi
d = math.pi / 8
while x <= math.pi:
	y = ((math.sin(x)) ** 2) + math.cos(x)
	print(y)
	x += d