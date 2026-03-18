a = int(input())
sum = 0
for i in range(len(str(a))):
    last = a % 10
    sum += last * (2 ** i)
    a //= 10

print(sum)
# b = int(str(a), 2)
# print(b)