n=int(input())
for i in range(n):
    leng=int(input())
    str1=input()
    result=False
    for i in str1[1:leng-1]:
        if str1.count(i)>1:
            result=True
            break
    if result:
        print("Yes")
    else:
        print("No")
