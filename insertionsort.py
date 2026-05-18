l=[7, 14, 19, 9, 88, 15, 61, 2, 99, 23]
for i in range(len(l)-1):
    min=i
    for j in l[i:]:
        if l[j]<l[min]:
            min=j
    if min(l[i:])!=l[i]:
        l[i], l[min]=l[min], l[j]