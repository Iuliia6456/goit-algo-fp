import random
from collections import defaultdict
from tabulate import tabulate

nums = 100000

counts = defaultdict(int)

for _ in range(nums):
    dice = random.randint(1, 6)
    dice_two = random.randint(1, 6)
    counts[dice + dice_two] += 1

probabilities = {key: count / nums for key, count in counts.items()}

headers = ["\nDice", "\nProbability"]
table = tabulate(probabilities.items(), headers=headers, tablefmt="fancy_grid", numalign="center", floatfmt=".2%")
print(table)
