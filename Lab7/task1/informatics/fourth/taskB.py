import math as m
a = int(input())
b = 2
while int(m.isqrt(a)) + 1 >= b:
    if a % b == 0:
        print(b)
        break
    b += 1
else:
    print(a)