def mergesort(arr):
    if len(arr)==0 or len(arr)==1:
        return arr
    mid=len(arr)//2
    lh=mergesort(arr[:mid])
    rh=mergesort(arr[mid:])
    i=0
    j=0
    l=[]
    while i<len(lh) and j<len(rh):
        if rh[j]<lh[i]:
            l.append(rh[j])
            j+=1
        elif lh[i]<rh[j]:
            l.append(lh[i])
            i+=1
        else:
            l.append(lh[i])
            i+=1
            l.append(rh[j])
            j+=1
    l.extend(rh[j:])
    l.extend(lh[i:])
    return l