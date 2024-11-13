# USACO 2018 February Contest, Bronze Problem 1. Teleportation
# https://usaco.org/index.php?page=viewproblem2&cpid=807

with open("teleport.in", "r") as f:
    start, end, tx, ty = map(int, f.readline().split())

res = min(abs(end - start), abs(tx - start) + abs(end - ty), abs(ty - start) + abs(tx - end))

with open("teleport.out", "w") as f:
    f.write(str(res))
    