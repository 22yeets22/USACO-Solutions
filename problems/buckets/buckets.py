# USACO 2019 US Open Contest, Bronze Problem 1. Bucket Brigade
# https://usaco.org/index.php?page=viewproblem2&cpid=939

# (needed help lol)

with open("buckets.in", "r") as f:
    farm_str = ''.join(f.read().splitlines())

barn_index = farm_str.index('B')  # no walrus operator because USACO only allows Python 3.6.9
barn = (barn_index % 10, barn_index // 10)  # Coordinates of the barn (x, y)
lake_index = farm_str.index('L')
lake = (lake_index % 10, lake_index // 10)  # Coordinates of the lake (x, y)
rock_index = farm_str.index('R')
rock = (rock_index % 10, rock_index // 10)  # Coordinates of the rock (x, y)

dist = abs(barn[0] - lake[0]) + abs(barn[1] - lake[1]) - 1  # Minimum distance

# The fastest path is always straight lines, but if they are all in the same row or column, we need 2 more cows
if (barn[0] == rock[0] == lake[0] and (barn[1] < rock[1] < lake[1] or barn[1] > rock[1] > lake[1])) or \
   (barn[1] == rock[1] == lake[1] and (barn[0] < rock[0] < lake[0] or barn[0] > rock[0] > lake[0])):
    dist += 2
elif dist == 0:
    dist = 2  # Right next to each other, two cows are needed

with open("buckets.out", "w") as f:
    f.write(str(dist))
