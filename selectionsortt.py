def selsort(arr):
    if len(arr)==1:
        return arr
    arrnew=selsort[arr[1:]]
    min=arr[0]
    minindex=0
    tempind=0
    while min<arrnew[i]:
        tempind+=1
    arrnew[minindex]=arrnew[tempind]
    arrnew[tempind]=min
    return arrnew