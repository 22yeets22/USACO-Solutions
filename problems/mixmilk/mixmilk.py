# USACO 2018 December Contest, Bronze Problem 1. Mixing Milk
# https://usaco.org/index.php?page=viewproblem2&cpid=855

with open("mixmilk.in", "r") as f:
    buckets = [list(map(int, f.readline().split())) for _ in range(3)]

for pour_num in range(100):
    current_bucket = pour_num % 3
    next_bucket = (current_bucket + 1) % 3
    
    buckets_current_volume = buckets[current_bucket][1] + buckets[next_bucket][1]
    next_bucket_volume = min(buckets[next_bucket][0], buckets_current_volume)  # Is the volume of the bucket smaller than what it can hold
    buckets[next_bucket][1] = next_bucket_volume
    buckets[current_bucket][1] = buckets_current_volume - next_bucket_volume  # Will there be extra left?

with open("mixmilk.out", "w") as f:
    f.write('\n'.join([str(i[1]) for i in buckets]))
