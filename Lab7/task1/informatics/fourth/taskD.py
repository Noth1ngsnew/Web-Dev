a = int(input())
b = 1
while b <= a:
    if b == a:
        print("YES")
        break
    b *= 2
else:
    print("NO")