import math

for i in range(0, 360, 10):
    n = i*math.pi/180
    a = math.cos(n)
    b = math.pow(a, 2)
    print(b)
