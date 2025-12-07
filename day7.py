# %%

from utils import load_advent_of_code

data = load_advent_of_code(202507)

print(data)
# %%
grid = {i + j * 1j: c for i, r in enumerate(data) for j, c in enumerate(r.strip())}
moves = [1, -1, 1j, -1j, 1 + 1j, -1 + 1j, 1 - 1j, -1 - 1j]
splits = [1, -1]
beamcol = set([data[0].index("S")])
# %%
splits = 0
for row in range(1, len(data)):
    newcol = set()
    splitcol = set()
    for col in beamcol:
        if data[row][col] == "^":
            splitcol.add(col)
            newcol.add(col + 1)
            newcol.add(col - 1)
        else:
            newcol.add(col)
    splits += len(splitcol)
    beamcol = newcol
print(splits)
# %%
from collections import defaultdict

split_spots = dict()
split_spots[0] = dict()
split_spots[0][data[0].index("S")] = 1
for row in range(1, len(data)):
    split_spots[row] = defaultdict(int)
    newcol = set()
    splitcol = set()
    for col in split_spots[row - 1]:
        if data[row][col] == "^":
            split_spots[row][col + 1] += split_spots[row - 1][col]
            split_spots[row][col - 1] += split_spots[row - 1][col]
        else:
            split_spots[row][col] += split_spots[row - 1][col]

# %%
