# %%
from collections import defaultdict

from utils import load_advent_of_code

data = load_advent_of_code(202511)

print(data)
# %%
pathdict = dict()
for line in data:
    key, vals = line.split(": ")
    pathdict[key] = [[vv, 1] for vv in vals.split(" ")]
more_paths = True
while more_paths:
    more_paths = False
    outpaths = defaultdict(int)
    for key, val in pathdict.items():
        if all([x[0] == "out" for x in val]):
            if key == "you":
                npaths = sum([x[1] for x in val])
                more_paths = False
                print(npaths)
                break
            else:
                outpaths[key] += sum([x[1] for x in val])
                if key == "dac" or key == "fft":
                    print(val, key)
                    print(outpaths[key])
                more_paths = True
    for key, startingvals in pathdict.items():
        newvals = []
        for pathout in startingvals:
            if pathout[0] in outpaths:
                newvals.append(["out", outpaths[pathout[0]]])
            else:
                newvals.append(pathout)
        pathdict[key] = newvals
# %%
pathdict = dict()
for line in data:
    key, vals = line.split(": ")
    pathdict[key] = [
        [vv, {"none": 1, "dac": 0, "fft": 0, "both": 0}] for vv in vals.split(" ")
    ]
more_paths = True
while more_paths:
    more_paths = False
    outpaths = dict()
    for key, val in pathdict.items():
        if all([x[0] == "out" for x in val]):
            if key not in outpaths:
                outpaths[key] = {"none": 0, "dac": 0, "fft": 0, "both": 0}
            if key == "svr":
                npaths = sum([x[1]["both"] for x in val])
                more_paths = False
                print(npaths)
                break
            elif key == "dac":
                outpaths[key]["none"] = 0
                outpaths[key]["fft"] = 0
                outpaths[key]["dac"] += sum([x[1]["none"] for x in val])
                outpaths[key]["both"] += sum([x[1]["fft"] for x in val])
                more_paths = True
            elif key == "fft":
                outpaths[key]["none"] = 0
                outpaths[key]["dac"] = 0
                outpaths[key]["fft"] += sum([x[1]["none"] for x in val])
                outpaths[key]["both"] += sum([x[1]["dac"] for x in val])
                more_paths = True

            else:
                outpaths[key]["none"] += sum([x[1]["none"] for x in val])
                outpaths[key]["dac"] = sum([x[1]["dac"] for x in val])
                outpaths[key]["fft"] += sum([x[1]["fft"] for x in val])
                outpaths[key]["both"] += sum([x[1]["both"] for x in val])
                more_paths = True
    for key, startingvals in pathdict.items():
        newvals = []
        for pathout in startingvals:
            if pathout[0] in outpaths:
                newvals.append(["out", outpaths[pathout[0]]])
            else:
                newvals.append(pathout)
        pathdict[key] = newvals
# logic is just to go back along out
# for all paths, count the outs and if they have seen either of those things yet
# so there is a dict that just has dac, fft, both, none

# %%
