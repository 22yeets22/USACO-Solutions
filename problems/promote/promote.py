# USACO 2016 January Contest, Bronze Problem 1. Promotion Counting
# https://usaco.org/index.php?page=viewproblem2&cpid=591

with open("promote.in", "r") as f:
    # Read all of the before and afters
    bronze_before, bronze_after = map(int, f.readline().split())
    silver_before, silver_after = map(int, f.readline().split())
    gold_before, gold_after = map(int, f.readline().split())
    platinum_before, platinum_after = map(int, f.readline().split())

platinum_promoted = platinum_after - platinum_before  # How many gold have been promoted to platinum
gold_promoted = gold_after - gold_before + platinum_promoted  # How many silver have been promoted to gold
silver_promoted = silver_after - silver_before + gold_promoted  # How many bronze have been promoted to silver

with open("promote.out", "w") as f:
    f.write('\n'.join([str(silver_promoted), str(gold_promoted), str(platinum_promoted)]))
