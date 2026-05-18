t = int(input())

for i in range(t):
    l = input().split()
    n = int(l[0])
    m = int(l[1])
    
    if n==1 or m==1:
        print("NO")
    elif n==2 and m==2:
        print("NO")
    else:
        print("YES")