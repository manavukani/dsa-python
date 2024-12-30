def jump_game(nums):
    reach = 0
    for i in range(len(nums)):
        # not reachable
        if i > reach:
            return False

        # update farthest reachable index
        reach = max(reach, i + nums[i])

    # can reach or exceed the last index
    return reach >= len(nums) - 1


nums = [1, 2, 0, 1, 0]
print(jump_game(nums))