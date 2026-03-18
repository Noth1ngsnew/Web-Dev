a = int(input())

sum = 0

for i in range(len(str(a))):
    sum += a % 10
    a //= 10

print(sum)