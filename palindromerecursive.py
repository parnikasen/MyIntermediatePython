def pal(str):
    if len(str)==0:
        return False
    if len(str)==1:
        return str
    if str[0]==str[-1]:
        if pal(str[1:-1]):
            return str
        else:
            return False
    else:
        return False
def printpals(str):
    for i in range(len(str)):
        for j in range(0, len(str)+1):
            if pal(str[i:j]):
                print(pal(str[i:j]))
                