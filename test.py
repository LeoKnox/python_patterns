def swapGreater(a):
    if a[0] > a[1]:
        a[0], a[1] = a[1], a[0]
        print(a)
    else:
        print(a)

alist = [6, 5, 9, 3, 1, 8]
swapGreater(alist)