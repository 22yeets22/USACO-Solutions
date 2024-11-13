# USACO 2016 December Contest, Bronze Problem 3. The Cow-Signal
# https://usaco.org/index.php?page=viewproblem2&cpid=665

with open("cowsignal.in", "r") as f:
    _, _, k = map(int, f.readline().split())
    signal = f.readlines()

new_signal = ''
for line in signal:
    new_line = ''
    for char in line.rstrip():
        new_line += char * k
    new_line += '\n'
    new_signal += new_line * k
new_signal = new_signal.strip()

with open("cowsignal.out", "w") as f:
    f.write(new_signal)
