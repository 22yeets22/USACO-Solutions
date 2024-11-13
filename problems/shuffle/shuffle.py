# USACO 2017 December Contest, Bronze Problem 2. The Bovine Shuffle
# https://usaco.org/index.php?page=viewproblem2&cpid=760


with open("shuffle.in", "r") as f:
    cow_count = int(f.readline())
    shuffle = [int(i) - 1 for i in f.readline().split()]
    cow_order = list(map(int, f.readline().split()))

# Shuffle 3 times (indexes are implicitly increasing)
for _ in range(3):
    cow_order = [cow_order[shuffle[i]] for i in range(cow_count)]

with open("shuffle.out", "w") as f:
    f.write('\n'.join(map(str, cow_order)))
