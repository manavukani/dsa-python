# initially positioned at the array's first index
# each element in the array represents your maximum jump length at that position
# reture True if can reach last index

'''
IMP ---> 2 cases:
- if no zero -> always reach end
- if zero -> may get stuck

eg: 2 3 1 1 0 5 2

cannot cross 0

APPROARCH:
- keep track of max idx we can reach
- if at any iteratiion, current idx > max index, return False
'''

def jump_game(arr):
    max_idx = 0
    for i, val in enumerate(arr):
        if i > max_idx:
            return False
        
        max_idx = max(max_idx, i + val)
    
    return True

#nums = [4, 3, 0, 7, 1, 2]
nums = [4, 3, 1, 1, 0, 7, 1, 2]
print(jump_game(nums))