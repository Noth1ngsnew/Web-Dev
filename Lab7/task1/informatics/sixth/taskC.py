def xor(x, y):
    if x == y:
        return 0
    else:
        return 1

x, y = map(int, input().split())
print(xor(x, y))