# USACO 2020 December Contest, Bronze Problem 1. Do You Know Your ABCs?
# https://usaco.org/index.php?page=viewproblem2&cpid=1059

from sys import stdin, stdout

nums = [int(n) for n in stdin.readline().split()]

# find max num, which is A+B+C
abc = max(nums)
nums.remove(abc)

# now there are 6 choose 3 = 20 combinations left
for i1, n1 in enumerate(nums):
    for i2, n2 in enumerate(nums):
        for i3, n3 in enumerate(nums):
            if i1 != i2 != i3 and n1 <= n2 <= n3 and n1 + n2 + n3 == abc:
                stdout.write(f"{nums[i1]} {nums[i2]} {nums[i3]}")
                exit()
