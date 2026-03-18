import math
a = int(input())

for i in range(2, int(math.isqrt(a)) + 1):
    if a % i == 0:
        print(i)
        break