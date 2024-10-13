# 1. Print All the Subsequence
# 2. Print all Subsequence which sums to K
def printSum(index, ds, nums, s, sum):
    if index == len(nums):
        if s == sum:
            print(ds)
        return

    ds.append(nums[index])
    s += nums[index]
    printSum(index+1, ds, nums, s, sum)
    ds.pop()
    s -= nums[index]
    printSum(index+1, ds, nums, s, sum)


print("printSum")
printSum(0, [], [1, 2, 1], 0, 2)

# 3. Print only 1st subseq which sums to K


def printOnlyOne(index, ds, nums, s, sum):
    if index == len(nums):
        if s == sum:
            print(ds)
            return True
        else:
            return False

    ds.append(nums[index])
    s += nums[index]
    # avoid future calls
    if printOnlyOne(index + 1, ds, nums, s, sum) == True:
        return True
    s -= nums[index]
    ds.pop()
    # avoid future calls
    if printOnlyOne(index + 1, ds, nums, s, sum) == True:
        return True

    return False


print("printOnlyOne")
printOnlyOne(0, [], [1, 2, 1], 0, 2)

# 4. Print the count of Sq which sums to K


def printCount(index, nums, s, sum):
    if s > sum:
        return 0
    if index == len(nums):
        if s == sum:
            return 1
        else:
            return 0
        
    s += nums[index]
    l = printCount(index+1, nums, s, sum)
    s -= nums[index]
    r = printCount(index+1, nums, s, sum)    
    total = l + r
    return total

print("printCount")
print(printCount(0, [1, 2, 1], 0, 2))
