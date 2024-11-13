# USACO 2015 December Contest, Bronze Problem 2. Speeding Ticket
# https://usaco.org/index.php?page=viewproblem2&cpid=568

with open("speeding.in", "r") as f:
    road_segments, driving_segments = map(int, f.readline().split())  # READ FILES
    roads = []
    for _ in range(road_segments):
        length, speed = map(int, f.readline().split())
        roads.extend([speed] * length)

    drives = []
    for _ in range(driving_segments):
        length, speed = map(int, f.readline().split())
        drives.extend([speed] * length)

max_speeding = 0
for pos in range(100):
    if roads[pos] < drives[pos]:
        max_speeding = max(max_speeding, drives[pos] - roads[pos])
max_speeding = max(max_speeding, 0)

with open("speeding.out", "w") as f:
    f.write(str(max_speeding))
