# USACO 2020 January Contest, Bronze Problem 1. Word Processor
# https://usaco.org/index.php?page=viewproblem2&cpid=987

with open("word.in", "r") as f:
    _, max_line_length = map(int, f.readline().split())  # READ FILES
    essay = f.readline().strip().split()

formatted = ''
current_line_length = 0
for word in essay:
    if current_line_length + len(word) > max_line_length:
        formatted += '\n'
        current_line_length = 0
    elif current_line_length != 0:
        formatted += ' '  # spaces do not count towards length

    formatted += word
    current_line_length += len(word)

with open("word.out", "w") as f:
    f.write(formatted)
