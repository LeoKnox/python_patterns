arr = [57, 57, -57, 57]

first = -60
second = -60

for i in arr:
    if i > first:
        second = first
        first = i
    elif i > second and i!=first:
        second = i
print (second)