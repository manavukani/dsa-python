# input -> accounts[i] is a list of strings, accounts[i][0] = name, rest = emails
# 2 account belong to same person, if 1 common email is there
# output -> result[i] is list of strings, result[i][0] = name and rest = emails in sorted order


from collections import defaultdict


class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x

    def union(self, x1, x2):
        p1, p2 = self.find(x1), self.find(x2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True


def accountsMerge(accounts):
    """
    APPROACH:
    1. map of email and what account it belongs to
        - if email repeats, union it with old occurrence
        - else, add to map
    2. regroup email by the main account
    3. Prepare response to required format - [[accountName, sortedEmails,....], ....]

    =================================================================
    TC: O(N+E) + O(E*4*aplha) + O(N*(E logE + E))
    where, N = no. of indices or nodes and E = no. of emails.
    - O(N+E)            : visiting all the emails.
    - O(E*4*aplha)      : merging the accounts.
    - O(N*(E logE + E)) : sorting the emails and storing them in the answer array.
    =================================================================
    SC: O(N)+ O(N) +O(2N) ~ O(N)
    where, N = no. of nodes/indices

    """
    n = len(accounts)
    uf = UnionFind(n)
    emailToAcc = {}  # email -> index of acc

    # Step 1 =====> O(E*4*aplha)
    for idx, acc in enumerate(accounts):
        for email in acc[1:]:  # 0th index = name
            if email in emailToAcc:
                uf.union(idx, emailToAcc[email])
            else:
                emailToAcc[email] = idx

    # Step 2 =====> O(N+E)
    emailGroup = defaultdict(list)  # index of acc -> list of emails
    for email, idx in emailToAcc.items():
        parent = uf.find(idx)
        emailGroup[parent].append(email)

    # Step 3 ======> O(N*(E log E + E))
    res = []
    for i, emails in emailGroup.items():
        name = accounts[i][0]
        res.append([name] + sorted(emailGroup[i]))  # array concat
    return res


accounts = [
    ["John", "j1@com", "j2@com", "j3@com"],  # 0
    ["John", "j4@com"],  # 1
    ["Raj", "r1@com", "r2@com"],  # 2
    ["John", "j1@com", "j5@com"],  # 3 ---> 0
    ["Raj", "r2@com", "r3@com"],  # 4 ---> 2
    ["Mary", "m1@com"],  # 5
]

print(accountsMerge(accounts))
