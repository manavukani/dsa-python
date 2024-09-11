def brute_force(arr):
    n = len(arr)
    max_freq, min_freq, max_ele, min_ele = 0, n, 0, 0

    visited = [False] * n
    for i in range(n):
        # Skip this element if already processed
        if visited[i] == True:
            continue

        # count frequency of element
        count = 1
        for j in range(i + 1, n):
            if (arr[i] == arr[j]):
                visited[j] = True
                count += 1

        if count > max_freq:
            max_ele = arr[i]
            max_freq = count

        if count < min_freq:
            min_ele = arr[i]
            min_freq = count

        # print(arr[i], count)

    return max_ele, min_ele


input = [10, 5, 10, 15, 10, 5]

print(brute_force(input))
