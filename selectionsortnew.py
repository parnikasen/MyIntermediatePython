def selsort(arr):
    minind=0
    i=0
    n=len(arr)
    if n==1:
        return arr
    while i<n:
        if arr[minind]>arr[i]:
            minind=i
        i+=1
    arr[minind], arr[0]=arr[0], arr[minind]
    first=arr[0]
    restsort=selsort(arr[1:])
    restsort.insert(0, first)
    return restsort