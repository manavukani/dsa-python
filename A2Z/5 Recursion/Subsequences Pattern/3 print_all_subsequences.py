# using recursion - parameterized
# TC: 2^n --- for every element we have 2 choices
# SC: O(n) --- recursion stack
def solve(index, arr, ds):
    if index >= len(arr):
        print(ds)
        return

    # pick
    ds.append(arr[index])
    solve(index + 1, arr, ds)
    ds.pop()
    
    # not pick
    solve(index + 1, arr, ds)


arr = [3, 1, 2]
# first 4 are printed by left tree (pick) and last 4 are printed by right tree (not pick)
solve(0, arr, [])


# functional recursion
def solve_functional(arr):
    """
    Generate the power set (all possible subsets) of a given list.
    This function uses functional recursion to generate all possible subsets of the input list.
    It works by splitting the list into the first element and the rest of the list, then recursively
    generating the power set of the rest of the list. It combines subsets that include the first element
    with those that do not.
    """
    if not arr:
        return [[]]

    first = arr[0]
    rest = arr[1:]

    without_first = solve_functional(rest)
    with_first = [[first] + subset for subset in without_first]

    return with_first + without_first


arr = [3, 1, 2]
print(solve_functional(arr))