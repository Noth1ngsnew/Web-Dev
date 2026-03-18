a = int(input())
reversedNum = ""
for i in range(len(str(a))):
    reversedNum += str(a % 10)
    a //= 10
print(int(reversedNum))

