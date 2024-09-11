# Count frequency of each element in the array

input = [1, 2, 8, 3, 2, 2, 2, 5, 1]


def brute_force(arr):
    for i in arr:
        count = 0
        for j in arr:
            if i == j:
                count += 1
        print(i, count)


brute_force(input)  # but this print multiple times for same element

print("**********")

# removing duplicates


def brute_force_2(arr):

    n = len(arr)
    visited = [False] * n

    for i in range(n):
        if (visited[i] == True):
            continue  # skip if already visited

        # initialize count for unvisited element
        count = 1

        # count frequency of element
        for j in range(i + 1, n):
            if (arr[i] == arr[j]):
                visited[j] = True  # mark as visited
                count += 1

        print(arr[i], count)


brute_force_2(input)

print("**********")

# OPTIMIZE: using hashing


def frequency_of_each(arr):
    freq = {}
    for i in arr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq


result = frequency_of_each(input)

print(result, "\n")

for x in result:
    print(x, result[x])
