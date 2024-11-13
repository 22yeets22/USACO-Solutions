# USACO 2016 January Contest, Bronze Problem 2. Angry Cows
# https://usaco.org/index.php?page=viewproblem2&cpid=592

with open("angry.in", "r") as f:
    n = int(f.readline())
    bales = [int(line.strip()) for line in f.readlines()]
    bales.sort()


def bales_exploded(bales, start_bale, direction):
    # Returns the farthest index reached by the explosion chain
    current_index = start_bale
    blast_radius = 1
    last_exploded = start_bale
    
    while True:
        next_index = current_index
        # Check bales within current blast radius
        while (0 <= next_index + direction < len(bales) and 
               abs(bales[next_index + direction] - bales[current_index]) <= blast_radius):
            next_index += direction
            
        # If no new bales exploded at this radius, stop
        if next_index == current_index:
            break
            
        # Update for next iteration
        current_index = next_index
        blast_radius += 1
        last_exploded = current_index
        
    return last_exploded


max_bales = 0
for start in range(len(bales)):
    # Get leftmost and rightmost explosion indices
    left_most = bales_exploded(bales, start, -1)
    right_most = bales_exploded(bales, start, 1)

    # Count total bales exploded
    current_bales = right_most - left_most + 1
    max_bales = max(max_bales, current_bales)
 
with open("angry.out", "w") as f:
    f.write(str(max_bales))
