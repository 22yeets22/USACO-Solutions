from sys import stdin

buckets = [[int(i) for i in stdin.readline().split()] for _ in range(5)]
#buckets = [[10, 2], [2, 2], [4, 1], [5, 4], [10, 1]]

for bucket_idx in range(len(buckets) - 1):
    current_capacity, current_volume = buckets[bucket_idx]
    next_capacity, next_volume = buckets[bucket_idx + 1]

    # Calculate the maximum amount of water we can pour
    pour_amount = min(current_volume, next_capacity - next_volume)
    
    # Pour the water
    buckets[bucket_idx][1] -= pour_amount
    buckets[bucket_idx + 1][1] += pour_amount


print(' '.join([str(vol) for _, vol in buckets]))
