from typing import List


# Time complexity: O(n*log(n))+O(n)
# Space Complexity: O(n) 
def removeDuplicates(nums: List[int]) -> int:
    unique_items = set()
    for i in nums:
        unique_items.add(i)
    
    k = len(unique_items)

    j = 0

    for item in unique_items:
        nums[j] = item
        j += 1
    return k


# We can think of using two pointers ‘i’ and ‘j’, we move ‘j’ till we don't get a number arr[j] which is different from arr[i].
# As we got a unique number we will increase the i pointer and update its value by arr[j]. 
# After completion of the loop return i+1, i.e size of the array of unique elements.

# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal(nums: List[int]) -> int:
    i = 0
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    return i + 1



if __name__ == "__main__":
    # arr = [1, 1, 2, 2, 2, 3, 3]
    arr = [0,0,1,1,1,2,2,3,3,4]
    k = optimal(arr)
    print("The array after removing duplicate elements is ")
    for i in range(k):
        print(arr[i], end=" ")
    print("\nUnique elements")
    print(k)
