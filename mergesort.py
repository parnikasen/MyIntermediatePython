def mergesort(arr):
    if len(arr)==1:
        return arr
    
    mid=len(arr)//2
    firsthalf=arr[:mid]
    secondhalf=arr[mid:]
    firsthalf= mergesort(firsthalf)
    secondhalf= mergesort(secondhalf)
    i=0
    j=0
    l=[]
    while i<len(firsthalf) and j<len(secondhalf):
        if firsthalf[i]>secondhalf[j]:
            l+=[secondhalf[j]]
            j+=1
        elif firsthalf[i]<secondhalf[j]:
            l+=[firsthalf[i]]
            i+=1
        else:
            l+=[firsthalf[i]]
            l+=[secondhalf[j]]
            i+=1
            j+=1
    l.extend(firsthalf[i:])
    l.extend(secondhalf[j:])

    return(l)