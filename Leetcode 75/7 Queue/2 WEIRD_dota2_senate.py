# input: senate = "RDDDRDRRDR"
# output: "Radiant"

# operations:
# 1. Radiant bans D or Dire bans R ---> If a senator is banned, he can't vote again
#                                  ---> If a senator is banned, the next senator in the round will vote
# 2. If a group has majority, it can annouce the victory
# NOTE: At each step, senator choose the most optimal decision among 2 options

# approach:
# - Greedily chooses to ban the next active senator from the other party
# - Use two queues to store the index of R and D
# - since voting is in round, after vote, the senator is sent to the end of queue
# - loser senator is removed from the queue
# - if the queue is empty, the other team wins


from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        radiant = deque()
        dire = deque()
        n = len(senate)

        # build the queues
        for i in range(n):
            if senate[i] == "R":
                radiant.append(i)
            else:
                dire.append(i)

        # voting process
        while radiant and dire:
            # R before D in queue (string), append to end of queue (string)
            if radiant[0] < dire[0]:
                radiant.append(radiant[0] + n)
            else:
                dire.append(dire[0] + n)
            # pop both, the winner will be eventually at end of queue
            radiant.popleft()
            dire.popleft()

        return "Radiant" if radiant else "Dire"
