a = int(input())
b = int(input())

for i in range(a,b + 1):
    root = int(i ** (1/2))
    if root * root == i:
        print(i)
