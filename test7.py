condition = True

num1 = 100_000
num2 = 100000

x = 1 if num1 == num2 else 0

for index, i in enumerate(str(num2)):
    print(index, i)

'''
if condition:
    x = 1
else:
    x = 0
'''

print(x)