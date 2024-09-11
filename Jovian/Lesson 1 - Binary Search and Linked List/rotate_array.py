def rotate_right(nums, k):
    n = len(nums)
    if n == 0:
        return nums

    k = k % n

    while k > 0:
        pick = nums[n - 1]

        for i in range(n - 1, 0, -1):
            nums[i] = nums[i - 1]  # rotate left -> nums[i-1] = nums[i]

        nums[0] = pick  # rotate left -> nums[n-1] = pick

        k -= 1

    return nums


print("-------BRUTE FORCE-------")
print("Rotated:", rotate_right([1, 2, 3, 4, 5], 0))


def optimal_rotate(nums, k):
    def reverse(nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    n = len(nums)
    k = k % n

    # Reverse the entire array
    reverse(nums, 0, n - 1)
    print(nums)
    # Reverse the first part
    reverse(nums, 0, k - 1)
    print(nums)
    # Reverse the second part
    reverse(nums, k, n - 1)
    print(nums)

    return nums


print("-------OPTIMAL-------")
print("Rotated:", optimal_rotate([1, 2, 3, 4, 5], 3))
