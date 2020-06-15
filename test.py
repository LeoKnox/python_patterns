def swapGreater(a):
    if a[0] > a[1]:
        a[0], a[1] = a[1], a[0]
        print(a)
    else:
        print(a)

def quickSort(a):
    if len(a) == 1:
        print(a)
    else:
        print(a)
        quickSort(a[0:len(a)-1])

alist = [6, 5, 9, 3, 1, 8]
blist = [6, 5]
clist = [6]
quickSort(alist)
swapGreater(alist)