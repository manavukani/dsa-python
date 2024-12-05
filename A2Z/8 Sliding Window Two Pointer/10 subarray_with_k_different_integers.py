# no. of subarray with k different int

# 1 2 1 3 4 -> [1,2,1], [1,3,4], [2,1,3]


# brute - generate all subarray - O(N^2)
def brute(arr, k):
    cnt = 0
    for i in range(len(arr)):
        mpp = {}
        for j in range(i, len(arr)):
            mpp[arr[j]] = 1 + mpp.get(arr[j], 0)
            if len(mpp) == k:
                cnt += 1
            if len(mpp) > k:
                break
    return mpp

# 2 1 1 1 3 4 3 2
# l
# r

