# %%

from utils import load_advent_of_code

data = load_advent_of_code(202508)

print(data)
# %%
import numpy as np

coord_list = [[int(q) for q in x.split(",")] for x in data]
coords = np.array(coord_list)
distances = np.zeros((3, (len(data) ** 2 - len(data)) // 2))

counter = 0
for ii in range(len(data)):
    for jj in range(ii + 1, len(data)):
        distances[0, counter] = ii
        distances[1, counter] = jj
        distances[2, counter] = np.linalg.norm(coords[ii] - coords[jj])
        counter += 1
# %%
sorted_indices = np.argsort(distances[2, :])
sorted_distances = distances[:, sorted_indices]

# %%
# junction is a node; circuit glues all of them
circuit_for_junction = {ii: ii for ii in range(1000)}
junctions_in_circuit = {ii: set([ii]) for ii in range(1000)}

for ii in range(1000):
    # get both junctions, figure out their circuit numbers, and whichever is lower, convert the higher to the lower
    j1 = sorted_distances[0, ii]
    j2 = sorted_distances[1, ii]
    if circuit_for_junction[j1] == circuit_for_junction[j2]:
        continue
    deprecated_circuit = max(circuit_for_junction[j1], circuit_for_junction[j2])
    base_circuit = min(circuit_for_junction[j1], circuit_for_junction[j2])
    for junction in junctions_in_circuit[deprecated_circuit]:
        circuit_for_junction[junction] = base_circuit
    junctions_in_circuit[base_circuit].update(junctions_in_circuit[deprecated_circuit])
    del junctions_in_circuit[deprecated_circuit]

# %%
junctions_sorted = sorted(junctions_in_circuit.items(), key=lambda x: len(x[1]))

# %%
len(junctions_sorted[-1][1]) * len(junctions_sorted[-2][1]) * len(
    junctions_sorted[-3][1]
)

# %%
# junction is a node; circuit glues all of them
circuit_for_junction = {ii: ii for ii in range(1000)}
junctions_in_circuit = {ii: set([ii]) for ii in range(1000)}
junctions_sorted = sorted(junctions_in_circuit.items(), key=lambda x: len(x[1]))
ii = -1
while len(junctions_in_circuit) > 1:
    ii += 1
    # get both junctions, figure out their circuit numbers, and whichever is lower, convert the higher to the lower
    j1 = sorted_distances[0, ii]
    j2 = sorted_distances[1, ii]
    if circuit_for_junction[j1] == circuit_for_junction[j2]:
        continue
    deprecated_circuit = max(circuit_for_junction[j1], circuit_for_junction[j2])
    base_circuit = min(circuit_for_junction[j1], circuit_for_junction[j2])
    for junction in junctions_in_circuit[deprecated_circuit]:
        circuit_for_junction[junction] = base_circuit
    junctions_in_circuit[base_circuit].update(junctions_in_circuit[deprecated_circuit])
    del junctions_in_circuit[deprecated_circuit]
print(sorted_distances[0, ii], sorted_distances[1, ii])

print(coords[0, sorted_distances[0, ii]] * coords[0, sorted_distances[1, ii]])

# %%
