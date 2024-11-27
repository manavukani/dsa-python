"""

positive - move right
negative - move left
value - size
speed - same for all

Find out the state of the asteroids after all collisions. 
If two asteroids meet, the smaller one will explode.
If both are the same size, both will explode.
Two asteroids moving in the same direction will never meet.

Eg1:
[5,10,-5] => [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

Eg2:

4 7 1 1 2 -3 -7 17 15 -16
4 7 1     -3 -7 17 15 -16
4 7       -3 -7 17 15 -16
4 7          -7 17 15 -16
4 7          -7 17 15 -16
4               17 15 -16
4               17    -16
4               17

OUTPUT = [4,17]

"""

# traverse until reach a -ve value
# compare with last +ve value and compare

# TC = O(2N) -> O(N) - for loop + O(N) - while loop max N times coz we add N elements
def solve(arr):
    stack = []
    n = len(arr)
    for i in range(n):
        if arr[i] > 0:
            stack.append(arr[i])
        else:
            while stack and stack[-1] > 0 and stack[-1] < abs(arr[i]):
                stack.pop()
            # stack empty or no collision
            if stack and stack[-1] == abs(arr[i]):
                # destroy both
                stack.pop()
            # only when stack empty -> add -ve ele to stack
            elif not stack or stack[-1] < 0:
                stack.append(arr[i])
    return stack


# GPT
class Solution:
    def asteroidCollision(self, asteroids):
        # Key observation: iterate through ENTIRE array, not just len-1
        stack = []
        
        for asteroid in asteroids:
            # Collision happens when:
            # 1. Current asteroid moves left (negative)
            # 2. Top of stack moves right (positive)
            while stack and asteroid < 0 < stack[-1]:
                # Compare absolute values of asteroids
                if stack[-1] < abs(asteroid):
                    # Current asteroid is larger, remove top of stack
                    stack.pop()
                    continue  # Continue checking stack
                elif stack[-1] == abs(asteroid):
                    # Equal sized asteroids, both destroyed
                    stack.pop()
                    break
                else:
                    # Top of stack asteroid is larger, current asteroid destroyed
                    break
            else:
                # No collision or asteroid survives
                stack.append(asteroid)
        
        return stack