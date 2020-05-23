x = [5,3,4,2,7,5,8,4,9]
y = [i for i in x if i%2 == 0]
print(y)

a = ['a', 'b', 'c']
b = {c: [i for i in x] for c in a}
print(b)