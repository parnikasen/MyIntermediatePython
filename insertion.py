def ins(arr):
    if len(arr)==1:
        return arr
    sortpart=ins(arr[:-1])
    curdig=arr[-1]
    i=0
    while curdig>arr[i]:
        i+=1
    return arr.insert(i, curdig)