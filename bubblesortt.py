def bubblesort(arr):
    i=0
    n=len(arr)
    swap=False
    if n==1:
        return arr
    while i<n:
        if arr[i]>arr[i+1]:
            arr[i], arr[i+1]=arr[i+1], arr[i]
            swap=True
        i+=1
    last=arr[-1]
    if swap:
        restsort=bubblesort(arr[:-1])
        restsort.append(last)
        return restsort
    else:
        return arr