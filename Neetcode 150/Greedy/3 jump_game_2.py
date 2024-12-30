def jump_game_2(nums):
    left = 0
    right = 0
    jumps = 0
    
    # reaches or exceeds the last index
    while right < len(nums) - 1:
        # farthest position you can jump to
        reach = 0
        
        # new reach for each ele in window
        for i in range(left, right+1):
            reach = max(reach, i + nums[i])
        
        # update the window boundary
        left = right + 1
        right = reach
        
        jumps += 1
    
    return jumps