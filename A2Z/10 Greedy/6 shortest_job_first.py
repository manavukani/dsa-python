def avg_waiting_time(arr):
    arr.sort()
    t = 0
    wtTime = 0
    for i in arr:
        wtTime += t
        t += i
    
    return wtTime/len(arr)

arr = [4,3,7,1,2]
print(avg_waiting_time(arr))