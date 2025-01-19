class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        for i in range(len(flowerbed)):
            if (
                # index is empty
                flowerbed[i] == 0
                # if left is empty or index = 0 (coz left is out of index)
                and (i == 0 or flowerbed[i - 1] == 0)
                # if right is empty or index = last (coz right is out of index)
                and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)
            ):
                flowerbed[i] = 1
                n -= 1

                if n == 0:
                    return True
        return False