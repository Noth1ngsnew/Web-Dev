a = int(input())
sum = 0

for i in range(1, int(a**0.5) + 1):
    if a % i == 0:
        if i != a // i:
            sum += 2
        else:
            sum += 1

print(sum)