def printSub(index, ds, arr):
    if index == len(arr):
        print(ds)
        return
    
    ds.append(arr[index])
    printSub(index+1, ds, arr)
    ds.pop()
    printSub(index+1, ds, arr)

printSub(0, [], [[3, 1, 2]])