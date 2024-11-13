# USACO 2019 January Contest, Bronze Problem 1. Shell Game
# https://usaco.org/index.php?page=viewproblem2&cpid=891

with open("shell.in", "r") as f:
    swap_count = int(f.readline())
    swaps = []
    for _ in range(swap_count):
        swaps.append(list(map(int, f.readline().split())))

max_correct_guesses = 0
for correct_shell in range(3):
    shells = [''] * 3
    shells[correct_shell] = 'X'
    correct_guesses = 0
    for swap in swaps:
        shells[swap[0] - 1], shells[swap[1] - 1] = shells[swap[1] - 1], shells[swap[0] - 1]
        if shells[swap[2] - 1] == 'X':
            correct_guesses += 1
    max_correct_guesses = max(max_correct_guesses, correct_guesses)


with open("shell.out", "w") as f:
    f.write(str(max_correct_guesses))
