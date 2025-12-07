# %%

from utils import load_advent_of_code

data = load_advent_of_code(202504)

print(data)
# %%
grid = {i + j * 1j: c for i, r in enumerate(data) for j, c in enumerate(r.strip())}
moves = [1, -1, 1j, -1j, 1 + 1j, -1 + 1j, 1 - 1j, -1 - 1j]
# %%
total = 0
newgrid = grid.copy()
for cell in grid:
    if grid[cell] == "@":
        neigh = [grid.get(cell + move, "n") == "@" for move in moves].count(True)
        if neigh < 4:
            total += 1
print(total)
# %%
staticgrid = grid.copy()
changed = True
removed = 0
while changed:
    newgrid = staticgrid.copy()
    changed = False
    for cell in staticgrid:
        if staticgrid[cell] == "@":
            neigh = [staticgrid.get(cell + move, "n") == "@" for move in moves].count(
                True
            )
            if neigh < 4:
                newgrid[cell] = "."
                removed += 1
                changed = True
    staticgrid = newgrid.copy()
print(removed)
# %%

reduced_ranges = [ranges[0]]
current_range_line = 1
while current_range_line < len(ranges):
    if ranges[current_range_line][0] > reduced_ranges[-1][1]:
        reduced_ranges.append(ranges[current_range_line])
        current_range_line += 1
    elif ranges[current_range_line][1] <= reduced_ranges[-1][1]:
        current_range_line += 1
    else:
        reduced_ranges[-1][1] = ranges[current_range_line][1]
        current_range_line += 1

# %%
ingredients = sorted([int(line) for line in data if "-" not in line and len(line) > 0])
# %%
fresh = 0
current_range_line = 0
for ingredient in ingredients:
    if ingredient < reduced_ranges[current_range_line][0]:
        continue

    while (
        current_range_line != len(reduced_ranges) - 1
        and ingredient > reduced_ranges[current_range_line][1]
    ):
        current_range_line += 1

    if (
        reduced_ranges[current_range_line][0]
        <= ingredient
        <= reduced_ranges[current_range_line][1]
    ):
        fresh += 1

print(fresh)
# shapedict = dict()
# for ii in range(size):
#     for jj in range(size):
#         shapedict[(ii, jj)] = nn[(ii, jj)]

# %%
ntotal = 0
for rrange in reduced_ranges:
    ntotal += rrange[1] - rrange[0] + 1
print(ntotal)

# %%
