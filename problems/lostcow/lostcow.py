# USACO 2017 US Open Contest, Bronze Problem 1. The Lost Cow
# https://usaco.org/index.php?page=viewproblem2&cpid=735

with open("lostcow.in", "r") as file:
    john_position, bessie_position = map(int, file.readline().split())

initial_john_position = john_position
bessie_is_to_the_right = john_position < bessie_position
total_distance = 0
step = 1
while True:
    last_john_position = john_position
    john_position = step + initial_john_position
    total_distance += abs(john_position - last_john_position)

    if (john_position >= bessie_position and bessie_is_to_the_right) or \
       (john_position <= bessie_position and not bessie_is_to_the_right):
        total_distance -= abs(bessie_position - john_position)
        break

    step *= -2

with open("lostcow.out", "w") as file:
    file.write(str(total_distance))

