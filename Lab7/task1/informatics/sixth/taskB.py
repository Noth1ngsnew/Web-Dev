def power(a,n):
    return a ** n

line = input().split()
a, n = float(line[0]), int(line[1])
print(power(a, n))