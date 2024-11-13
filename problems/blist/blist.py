# USACO 2018 December Contest, Bronze Problem 2. The Bucket List
# https://usaco.org/index.php?page=viewproblem2&cpid=856

bucket_change = [0 for _ in range(1001)]
with open("blist.in", "r") as f:
    cows_count = int(f.readline())
    for _ in range(cows_count):
        start, end, amount = map(int, f.readline().split())
        bucket_change[start] += amount
        bucket_change[end] -= amount

max_buckets = 0
current_buckets = 0
for bucket in bucket_change:
    current_buckets += bucket
    max_buckets = max(max_buckets, current_buckets)

with open("blist.out", "w") as f:
    f.write(str(max_buckets))
