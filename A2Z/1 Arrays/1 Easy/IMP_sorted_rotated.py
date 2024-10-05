# if array is sorted and rotated then, there is only 1 break point where (nums[x] > nums[x+1]),
# if array is only sorted then, there is 0 break point.

def check(nums):
    count = 0
    n = len(nums)

    for i in range(1, n):
        if nums[i] < nums[i - 1]:
            count += 1

    # nums = [2,1,3,4]
    # result true without %n, but it is not sorted and rotated
    # we have to check last and first element also.
    if nums[-1] > nums[0]:
        count += 1

    return count <= 1


# instead of checking first and last explicitly we can use %
def check2(nums):
    count = 0
    n = len(nums)

    for i in range(n):
        if nums[i] > nums[(i + 1) % n]:
            count += 1

    return count <= 1


print(check([4, 1, 2, 3]))
print(check([2, 1, 3, 4]))
print(check2([2, 1, 3, 4]))
