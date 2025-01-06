# input = candidate numbers (candidates) and a target number (target)
# TODO: find all unique combinations in candidates where the candidate numbers sum to target.

# TWIST:
# - any candidates may only be USED ONCE in the combination.
# - must not contain duplicate combinations.
# - return in sorted order


def combination_sum_2(arr, target):
    """IMP: using set to remove duplicates"""
    ans = set()
    ds = []

    def generate_combinations(target, idx):
        if idx == len(arr):
            if target == 0:
                ans.add(tuple(ds))  # store combination as a tuple, list is not hashable
            return

        # pick
        if arr[idx] <= target:
            ds.append(arr[idx])
            generate_combinations(target - arr[idx], idx + 1)
            ds.pop()

        # IMPP ---> skip over duplicate elements in the recursive call to avoid repeated combinations.
        next_idx = idx + 1
        while next_idx < len(arr) and arr[next_idx] == arr[idx]:
            next_idx += 1

        # not pick
        generate_combinations(target, next_idx)

        return ans

    # sorting array places duplicate values consecutively, ez to skip
    # also ensures final result is in sorted order.
    arr.sort()
    generate_combinations(target, 0)

    return sorted(ans)  # sort and convert to list


arr = [10, 1, 2, 7, 6, 1, 5]
target = 8
print(combination_sum_2(arr, target))  # [(1, 1, 6), (1, 2, 5), (1, 7), (2, 6)]