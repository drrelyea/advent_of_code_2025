# %%

from utils import load_advent_of_code

data = load_advent_of_code(202503)

print(data)
# %%
jolts = 0
numlist = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
for line in data:
    newline = [int(x) for x in line]
    current_index = 0
    for digit in range(12):
        num_not_found = True
        numlist_index = 0
        while num_not_found:
            if (
                numlist[numlist_index]
                in newline[current_index : len(newline) - 11 + digit]
            ):
                num_not_found = False
                jolts += numlist[numlist_index] * 10 ** (11 - digit)
                current_index += (
                    newline[current_index : len(newline) - 11 + digit].index(
                        numlist[numlist_index]
                    )
                    + 1
                )
            numlist_index += 1
print(jolts)
# %%
