# use max operation and return True if target is achievable

# NOTE - if any triplet has any value > target, we cannot use it, it will overshoot target


def brute(triplets, target):
    x, y, z = 0, 0, 0
    ta, tb, tc = target

    for a, b, c in triplets:
        if a <= ta and b <= tb and c <= tc:
            x = max(x, a)
            y = max(y, b)
            z = max(z, c)
            if [x, y, z] == target:
                return True

    return False

# TC = O(N)
def solve(triplets, target):
    good = set()
    for t in triplets:
        # ignore triplets with bigger values
        if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
            continue

        for idx, val in enumerate(t):
            # if any matches target
            if val == target[idx]:
                good.add(idx)

    # got all 3 idx
    return len(good) == 3
