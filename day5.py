# %%

from utils import load_advent_of_code

data = load_advent_of_code(202505)

print(data)
# %%
ranges = [[int(x) for x in line.split("-")] for line in data if "-" in line]
ranges = sorted(ranges, key=lambda x: x[0])
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
