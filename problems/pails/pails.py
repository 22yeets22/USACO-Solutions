# USACO 2016 February Contest, Bronze Problem 1. Milk Pails
# https://usaco.org/index.php?page=viewproblem2&cpid=615

from math import ceil

with open("pails.in", "r") as f:
    small_pail, medium_pail, max_fill = map(int, f.readline().split())

best_fill = 0
for i in range(ceil(max_fill / small_pail)):
    for j in range(ceil(max_fill / medium_pail)):
        current_fill = i * small_pail + j * medium_pail
        if current_fill > max_fill:
            continue
        best_fill = max(current_fill, best_fill)

with open("pails.out", "w") as f:
    f.write(str(best_fill))
