# single lane road => cannot overtake
# cars are moving at different speeds
# each car has a unique start position
# input = target, position, speed
# output = number of car fleets that will arrive at the destination

# edge case: if two cars catch up at end, they are part of the same fleet

'''

target = 10
(pos, speed) = [(3,3),(5,2),(7,1)]

pos ==> 0 1 2 3 4 5 6 7 8 9 10
car ==>       A   B   C
spe ==>       3   2   1
ETA ==>      2.3 2.5  3

car B and C will form a fleet, as B reaches before C (faster)
we keep track of car that's ahead, as it limits the speed of fleet
--> so we go from right to left
--> cannot say if A will collide with B
as B might change the speed due to some car ahead of it

'''

# o(nlogn) time | o(n) space
def solve(target, position, speed):
    # add time to reach target in stack
    # if the new time is less than previous one, then pop it
    stack = []
    # sort and check from last (closest to target)
    for p, s in sorted(zip(position, speed), reverse=True):
        # time for car
        stack.append((target-p)/s)
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            # pop if its faster than any of previous (coz they will form fleet)
            stack.pop()
    return len(stack)


taregt = 12
position = [10, 8, 0, 5, 3]
speed = [2, 4, 1, 1, 3]
print(solve(taregt, position, speed))


def itertion(target, position, speed):
    pair = [(p, s) for p, s in zip(position, speed)]
    pair.sort(reverse=True)
    
    fleets = 1
    prevTime = (target - pair[0][0]) / pair[0][1]
    for i in range(1, len(pair)):
        currCar = pair[i]
        currTime = (target - currCar[0]) / currCar[1]
        if currTime > prevTime:
            fleets += 1
            prevTime = currTime
    return fleets