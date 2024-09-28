# Given an array of N integers, write a program to return an
# element that occurs more than N/2 times in the given array.
# You may consider that such an element always exists in the array.

# ================= brute force => double "for" loops => O(n^2)
def brute(arr):
    n = len(arr)
    # check count "for" each element
    for i in range(n):
        cnt = 0
        for j in range(n):
            if arr[j] == arr[i]:
                cnt += 1
        # Check if frequency is greater than n/2
        if cnt > (n // 2):
            return arr[i]

    return -1

# ================= better => counting so hash map => O(N) + O(N logN)


def better(arr):
    hash_map = {}
    # Insertion in the map => logN time, doing it for N elements => O(N logN)
    for i in range(len(arr)):
        if arr[i] in hash_map:
            hash_map[arr[i]] += 1
        else:
            hash_map[arr[i]] = 1

    # checking which element occurs more than floor(N/2) times => N
    for key, value in hash_map.items():
        if value > (len(arr) // 2):
            return key
    return -1


# ================= optimal => Moore's voting algorithm => O(N)
# 1. Find a candidate that may be the majority element
#    -> If count == 0, update candidate
#    -> If the current == candidate, count++
#    -> If the current != candidate, count--
# 2. Check if the candidate is actually the majority element

def optimal(arr):
    count = 0
    for i in range(len(arr)):
        if count == 0:
            candidate = arr[i]
            count = 1
        elif arr[i] == candidate:
            count += 1
        else:
            count -= 1
    
    # check if the candidate is actually the majority element
    cnt = 0
    for i in range(len(arr)):
        if arr[i] == candidate:
            cnt += 1
            
    if cnt > (len(arr) // 2):
        return candidate
    
    return -1


arr = [5,7,7,7,9,8,8,8,9,7,7]
ans = optimal(arr)
print("The majority element is:", ans)
