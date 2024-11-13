# USACO 2017 February Contest, Bronze Problem 3. Why Did the Cow Cross the Road III
# https://usaco.org/index.php?page=viewproblem2&cpid=713

with open("cowqueue.in", "r") as f:
    n = int(f.readline())
    cows = []
    for _ in range(n):
        cows.append([int(i) for i in f.readline().split()])
    cows.sort()

next_cow_time = 0
for cow in cows:
    start, length = cow
    next_cow_time = max(next_cow_time, start) + length

with open("cowqueue.out", "w") as f:
    f.write(str(next_cow_time))
