def printf(i, ds, arr, n):
    if i == n:
        print(ds)
        return

    # pick
    ds.append(arr[i])
    printf(i+1, ds, arr, n)
    ds.pop()

    # not pick
    printf(i+1, ds, arr, n)


arr = [3, 1, 2]
n = 3
ds = []
printf(0, ds, arr, n)
