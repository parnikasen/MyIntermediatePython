l=[42, 7, 19, 3, 88, 15, 61, 2, 99, 23]
for j in range(len(l)):
    swap=False
    for i in range(len(l)-j-1):
        if l[i]>l[i+1]:
            l[i],l[i+1]=l[i+1],l[i]
            swap=True
    if not swap:
        break
