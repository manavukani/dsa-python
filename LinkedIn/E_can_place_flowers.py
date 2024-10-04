def canPlaceFlowers(flowerbed, n):
    count = 0
    for i in range(len(flowerbed)):
        # Check if the current plot is empty.
        if flowerbed[i] == 0:
            # Check if the left and right plots are empty.
            # if left is empty or index = 0 (coz left is out of index)
            empty_left_plot = (i == 0) or (flowerbed[i - 1] == 0)
            # if right is empty or index = last (coz right is out of index)
            empty_right_lot = (i == len(flowerbed) -1) or (flowerbed[i + 1] == 0)

            # If both plots are empty, we can plant a flower here.
            if empty_left_plot and empty_right_lot:
                flowerbed[i] = 1
                count += 1

    # compare plantable spaces with n
    return count >= n
