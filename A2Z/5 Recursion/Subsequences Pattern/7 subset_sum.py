# list of sums of all possible subsets of an array

# APPROACH:
# pick - we add current ele to running_sum
# not pick - we don't, just move to next idx


def subset_sum(arr):
    ans = []

    def find_subset_sums(idx, running_sum):
        if idx == len(arr):
            ans.append(running_sum)
            return

        # pick - we add current ele + running_sum
        find_subset_sums(idx + 1, running_sum + arr[idx])

        # not pick
        find_subset_sums(idx + 1, running_sum)

    # calling recusion with idx=0 and running_sum=0
    find_subset_sums(0, 0)
    return ans


arr = [1, 2, 3]
print(subset_sum(arr))


# SUBSETS = [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]
# SUMS    =      6         3       4     1      5     2    3    0
