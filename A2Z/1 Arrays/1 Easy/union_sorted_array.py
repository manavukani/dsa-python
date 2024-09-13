'''
Approach: similar to merge in merge sort but we check if last added element is equal to new being added or not


=> using sorted array to decrease time complexity
=> O((m+n)log(m+n)) =>  O(m+n)

There may be cases like the element to be inserted is already present in the union, we are inserting duplicates which is not desired. 
So while inserting always check whether the last element in the union vector is equal or not to the element to be inserted. 
If equal we are trying to insert duplicates, so don't insert the element, else insert the element in the union. 
This makes sure that we are not inserting any duplicates in the union because we are inserting elements in sorted order.

'''

# ONLY FOR SORTED ARRAY
def solve(arr1, arr2):
    i, j = 0, 0
    union = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            if len(union) == 0 or union[-1] != arr1[i]:
                union.append(arr1[i])
            i += 1
        else:
            if len(union) == 0 or union[-1] != arr2[j]:
                union.append(arr2[j])
            j += 1

    while i < len(arr1):  # If any elements left in arr1
        if union[-1] != arr1[i]:
            union.append(arr1[i])
        i += 1

    while j < len(arr2):  # If any elements left in arr2
        if union[-1] != arr2[j]:
            union.append(arr2[j])
        j += 1

    return union

arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = [2, 3, 4, 4, 5, 11, 12]

union = solve(arr1, arr2)

print("Union of arr1 and arr2 is:")
print(union)


'''
Time Compleixty:

O( (m+n)log(m+n) )
=> Inserting an element in a set takes logN time, where N is no of elements in the set. 
=> At max set can store m+n elements {when there are no common elements and elements in arr,arr2 are distntict}. 
=> So Inserting m+n th element takes log(m+n) time. 
=> Upon approximation across inserting all elements in worst, it would take O((m+n)log(m+n) time.


=> Using HashSet also takes the same time, On average insertion in unordered_set takes O(1) time but sorting the union vector takes O((m+n)log(m+n))  time. Because at max union vector can have m+n elements.

Space Complexity: 

O(m+n) {If Space of Union ArrayList is considered} 

O(1) {If Space of union ArrayList is not considered}

'''

# using map
# use .get instead of freq[num] coz if DNE then it returns a default value (here - 0) instead of KeyError

def find_union_with_map(arr1, arr2):
    freq = {}
    union = []

    for num in arr1:
        # if exists +1 else initiate 0 then +1
        freq[num] = freq.get(num, 0) + 1

    for num in arr2:
        freq[num] = freq.get(num, 0) + 1

    for num in freq:
        union.append(num)

    return union

def find_union_with_set(arr1, arr2):
    s = set()
    union = []

    for num in arr1:
        s.add(num)

    for num in arr2:
        s.add(num)

    for num in s:
        union.append(num)

    return union

# WORKS WITH NON SORTED ARRAY AS WELL

arr3= [3,5,2,8]
arr4= [1,6,3,5,2,8]

# union = find_union_with_map(arr3, arr4)
union = find_union_with_set(arr3, arr4)

print("\nUnion of unsorted:", union)
