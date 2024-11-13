# USACO 2022 December Contest, Bronze Problem 1. Cow College
# https://usaco.org/index.php?page=viewproblem2&cpid=1251

from sys import stdin, stdout

cow_count = int(stdin.readline())
cows = [int(cow) for cow in stdin.readline().split()]
cows.sort()

max_sum_tuition = max_tuition = 0
for cow_num, cow_tuition in enumerate(cows):
    current_sum_tuition = (cow_count - cow_num) * cow_tuition
    if current_sum_tuition > max_sum_tuition:
        max_sum_tuition = current_sum_tuition
        max_tuition = cow_tuition

stdout.write(f"{max_sum_tuition} {max_tuition}")
