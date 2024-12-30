# given gas and cost for stations on circular track
# cost between i and i+1 is cost[i]
# gas refulled at i is gas[i]
# start with empty tank, find a starting point from whre you can complete a loop

# O(N^2)
def brute(gas, cost):
    n = len(gas)

    for i in range(n):
        tank = gas[i] - cost[i]
        if tank < 0:
            continue  # not possible, move to the next starting station
        j = (j + 1) % n
        # complete loop
        while j != i:
            tank += gas[j] - cost[j]
            if tank < 0:
                break  # move to the next starting station
            j += 1
            j %= n
        if j == i:  # full circle => i can be starting point
            return i
    return -1


# O(N)
def greedy(gas, cost):
    # check feasibility
    if sum(gas) < sum(cost):
        return -1

    tank = 0
    startingPt = 0
    for i in range(len(gas)):
        tank += gas[i] - cost[i]

        # if not possible, rest total & move to next starting index
        if tank < 0:
            tank = 0
            startingPt = i + 1
    return startingPt


"""
IMP: Why we dont need to check in circular manner

1. Greedy Strategy Leverages Local Optimality:
    - tracks current balance of tank, if the balance becomes negative at any station, it means we cannot start from any of the previous stations and complete the circuit because:
        - gas deficit accumulated up to that point cannot be compensated by starting from any of the earlier stations.
    - Therefore, we can confidently restart our search from the next station (start = i + 1).

2. Circular Nature is Handled Implicitly:
    - traverse the entire array linearly, simulate circular behavior without explicitly wrapping around.
    - traversal ends, if feasibility check is satisfied and no deficit occurs in the final cumulative balance,
    the last determined start is valid.

"""
