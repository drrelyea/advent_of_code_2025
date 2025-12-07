# %%

from utils import load_advent_of_code

data = load_advent_of_code(202501)

print(data)
# %%
data = [
    "L68",
    "L30",
    "R48",
    "L5",
    "R60",
    "L55",
    "L1",
    "L99",
    "R14",
    "L82",
]

# %%
start = 50
total = 0
for line in data:
    if line[0] == "L":
        start = (start - int(line[1:])) % 100
    elif line[0] == "R":
        start = (start + int(line[1:])) % 100
    if start == 0:
        total += 1

print(total)

# %%
start = 50
total = 0
for line in data:
    print(line)
    if line[0] == "L":
        if start - int(line[1:]) <= 0:
            total += (-1 * (start - int(line[1:])) // 100) + 1
            if start == 0:
                total -= 1
        start = (start - int(line[1:])) % 100
    elif line[0] == "R":
        if start + int(line[1:]) >= 100:
            total += (start + int(line[1:])) // 100
        start = (start + int(line[1:])) % 100
    print(total)
print(total)

# %%
