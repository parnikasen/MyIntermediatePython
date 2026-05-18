l=[7, 14, 19, 9, 88, 15, 61, 2, 99, 23]
for i in range(1, len(l)):
    key=l[i]
    j=i-1
    while j>=0 and l[j]>key:
        l[j+1]=l[j]
        j-=1
    l[j+1]=key