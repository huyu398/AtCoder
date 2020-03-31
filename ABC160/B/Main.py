X = int(input())

c500 = X // 500
X -= 500 * c500

c5 = X // 5
happy = c500 * 1000 + c5 * 5
print(happy)
