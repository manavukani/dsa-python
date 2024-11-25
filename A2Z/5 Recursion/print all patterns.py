def printS(i, ds, sum, s, arr, n):
    if i == n:
        if s == sum:
            print(ds)
        return

    # pick
    ds.append(arr[i])
    s += arr[i]
    printS(i+1, ds, sum, s, arr, n)
    s -= arr[i]
    ds.pop()

    # not pick
    printS(i+1, ds, sum, s, arr, n)

# what if i just want to print one pattern
def printS_justOne(i, ds, sum, s, arr, n):
    if i == n:
        # condition satisfied
        if s == sum:
            print(ds)
            return True
        # condition not satisfied
        else:
            return False

    # pick
    ds.append(arr[i])
    s += arr[i]
    
    if printS_justOne(i+1, ds, sum, s, arr, n):
        return True
        
    s -= arr[i]
    ds.pop()

    # not pick
    if printS_justOne(i+1, ds, sum, s, arr, n):
        return True

    
    # if none return true
    return False

def print_count(i, ds, sum, s, arr, n):
    if i == n:
        if s == sum:
            return 1
        else:
            return 0
    
    # pick
    ds.append(arr[i])
    s += arr[i]
    c1 = print_count(i+1, ds, sum, s, arr, n)
    s -= arr[i]
    ds.pop()
    
    # not picks
    c2 = print_count(i+1, ds, sum, s, arr, n)
    
    return c1 + c2



arr = [1,2,1]
n = 3
sum = 2
ds = []
printS(0, ds, sum, 0, arr, n)
print("======")
printS_justOne(0, ds, sum, 0, arr, n)
print("======")
print(print_count(0, ds, sum, 0, arr, n))
