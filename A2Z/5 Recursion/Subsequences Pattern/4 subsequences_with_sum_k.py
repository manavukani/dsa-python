# SUBSEQUENCES PATTERNS

""" --------- Subsequences with sum K --------- """


def subsequences_with_sum_k(arr, k, current_sum, ds, idx):
    if idx == len(arr):
        if current_sum == k:
            print(ds)
        return

    # pick
    ds.append(arr[idx])
    current_sum += arr[idx]
    subsequences_with_sum_k(arr, k, current_sum, ds, idx + 1)
    # unpick
    ds.pop()
    current_sum -= arr[idx]

    # not pick
    subsequences_with_sum_k(arr, k, current_sum, ds, idx + 1)


print("\nall subsequences with sum K")
subsequences_with_sum_k(arr=[1, 2, 1], k=2, current_sum=0, ds=[], idx=0)


""" --------- First Subsequences with sum K --------- """


def first_subsequence_with_k(arr, k, current_sum, ds, idx):
    if idx == len(arr):
        if current_sum == k:
            print(ds)
            return True
        return False

    # PICK
    ds.append(arr[idx])
    current_sum += arr[idx]
    if first_subsequence_with_k(arr, k, current_sum, ds, idx + 1):
        return True  # return to avoid future calls
    current_sum -= arr[idx]
    ds.pop()

    # NOT PICK
    if first_subsequence_with_k(arr, k, current_sum, ds, idx + 1):
        return True

    return False


print("\nfirst subsequence with sum K")
first_subsequence_with_k([1, 2, 1], 2, 0, [], 0)

""" --------- Count of total Subsequences with sum K --------- """


def count_subsequences_sum_k(arr, k, current_sum, idx):
    if current_sum > k:
        return 0  # terminate early if current sum exceeds k
    if idx == len(arr):
        if current_sum == k:
            return 1
        return 0

    # Count number of subsequences in both trees and return sum
    current_sum += arr[idx]
    l = count_subsequences_sum_k(arr, k, current_sum, idx + 1)
    current_sum -= arr[idx]
    r = count_subsequences_sum_k(arr, k, current_sum, idx + 1)
    total = l + r
    return total


print("\nNumber of subsequences with sum K")
print(count_subsequences_sum_k([1, 2, 1], 2, 0, 0))
