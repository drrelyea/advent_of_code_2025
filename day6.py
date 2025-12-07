# %%

from utils import load_advent_of_code

data = load_advent_of_code(202501)

print(data)
# %%
# nn = data_to_numpy(data)
# nn = nn.T

size = len(data)
print(size)
# size = 71


# shapedict = dict()
# for ii in range(size):
#     for jj in range(size):
#         shapedict[(ii, jj)] = nn[(ii, jj)]

# %%
datalist = []
for dataline in data:
    datalist.append(dataline.split())

total = 0
for iqq, qq in enumerate(datalist[-1]):
    if qq == "+":
        for datalistrow in datalist[:-1]:
            total += int(datalistrow[iqq])

    elif qq == "*":
        sum = 1
        for datalistrow in datalist[:-1]:
            sum *= int(datalistrow[iqq])
        total += sum
print(total)

# %%
new_data = data.copy()
new_data[4] += "  "
data_t = [list(row) for row in zip(*new_data)]
iline = 0
total = 0
while iline < len(data_t):
    the_line = data_t[iline]
    if the_line[-1] == "+":
        while "".join(the_line).strip():
            intline = int("".join(the_line).replace("+", "").strip())
            if iline > 3700:
                print(the_line, intline)
            total += intline
            iline += 1
            if iline == len(data_t):
                break
            the_line = data_t[iline]
    elif the_line[-1] == "*":
        sum = 1
        while "".join(the_line).strip():
            intline = int("".join(the_line).replace("*", "").strip())
            if iline > 3700:
                print(the_line, intline)
            sum *= intline
            iline += 1
            if iline == len(data_t):
                break
            the_line = data_t[iline]
        total += sum
    iline += 1
print(total)

# %%
