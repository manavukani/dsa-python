# ip: job-id, profit, deadline
# op:
# 1. maximum jobs that can be completed within deadlines
# 2. total maximum profit

"""
Obs:
- delay the jobs with big deadline, end will be empty
- do max profit job

Approach:
- sort by profits
- find max deadline we can extend to
- start filling from as much end as possible (delay the job)


TC: O(N log N) + O(N*M)

- O(N log N) for sorting the jobs
- O(N*M) for iterating over all jobs and checking from last deadline, M in the worst case.

SC: O(M), M = maximum deadline
"""


import heapq


class job:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit


class Solution:
    def jobScheduling(self, jobs):
        # sort by profits
        jobs.sort(key=lambda x: x.profit, reverse=True)

        # find max deadline we can extend to
        maxi = jobs[0].deadline
        for i in range(1, len(jobs)):
            maxi = max(maxi, jobs[i].deadline)

        # init array size with maxi + 1 (today + max deadlines)
        slot = [-1] * (maxi + 1)
        countJobs = 0
        jobProfit = 0

        # for all jobs
        for i in range(len(jobs)):
            # find empty spot, start from deadline ---> delay execution
            for j in range(jobs[i].deadline, 0, -1):
                if slot[j] == -1:  # empty day
                    slot[j] = i
                    countJobs += 1
                    jobProfit += jobs[i].profit
                    break

        return countJobs, jobProfit


jobs = [job(1, 4, 20), job(2, 1, 10), job(3, 2, 40), job(4, 2, 30)]
count, profit = Solution().jobScheduling(jobs)
print(f"Tasks Executed: {count}\nMax Profit Gained: {profit}")


# ====================== SAME BUT WITHOUT CLASSES ======================


def jobScheduling(id, deadline, profit):
    jobs = list(zip(id, deadline, profit))
    jobs.sort(key=lambda x: x[2], reverse=True)

    max_deadline = max(deadline)

    slots = [-1] * (max_deadline + 1)
    total_profit = 0
    jobs_done = 0

    for job_id, job_deadline, job_profit in jobs:
        for t in range(job_deadline, 0, -1):
            if slots[t] == -1:
                slots[t] = job_id
                total_profit += job_profit
                jobs_done += 1
                break

    return jobs_done, total_profit


id = [1, 2, 3, 4]
deadline = [4, 1, 2, 2]
profit = [20, 10, 40, 30]

jobs_done, total_profit = jobScheduling(id, deadline, profit)
print(f"Number of Jobs Done: {jobs_done}")
print(f"Total Profit: {total_profit}")


# ==================== MORE TIME OPTIMIZED - USING PRIORITY QUEUE, TC: O(NlogN) ===================
# can also use Disjoint Set Union - check GFG


def JobSequencing_pq(id, deadline, profit):
    n = len(id)
    jobs = [(id[i], deadline[i], profit[i]) for i in range(n)]

    jobs.sort(key=lambda x: x[1])

    # track least profitable jobs
    pq = []
    curr = 1

    for job in jobs:
        if job[1] >= curr:
            heapq.heappush(pq, job[2])
            curr += 1
        else:
            if pq and job[2] > pq[0]:
                heapq.heappushpop(pq, job[2])

    total_profit = sum(pq)
    job_count = len(pq)

    return [job_count, total_profit]
