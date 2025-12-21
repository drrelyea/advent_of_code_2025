# %%

from utils import load_advent_of_code

data = load_advent_of_code(202510)

print(data)
# %%
import re


def try_k_buttons(
    current_lights: set[int],
    the_buttons: list[set[int]],
    presses_left: int,
    truth: set[int],
    buttons_pressed: list[set[int]],
):
    # print(the_buttons, presses_left, truth)
    if presses_left == 0:
        return False
    for button in the_buttons:
        new_lights = current_lights.symmetric_difference(button)
        # print(buttons_pressed + [button], new_lights)
        if new_lights == truth:
            # print(truth, "and", buttons_pressed + [button])
            return True
        fewer_buttons = the_buttons.copy()
        fewer_buttons.remove(button)
        if try_k_buttons(
            new_lights,
            fewer_buttons,
            presses_left - 1,
            truth,
            buttons_pressed + [button],
        ):
            return True
    return False


# %%
total = 0
for iline, line in enumerate(data):
    print(iline)
    # lights = [x == "#" for x in line.split("[")[1].split("]")[0]]
    buttons = [
        set([int(x) for x in qq.split(")")[0].split(",")]) for qq in line.split("(")[1:]
    ]
    # null_buttons = [x == "rr" for x in line.split("[")[1].split("]")[0]]
    # binary_buttons = [null_buttons.copy() for _ in buttons]
    # for ibutton, button in enumerate(buttons):
    #     for light in button.split(","):
    #         binary_buttons[ibutton][int(light)] = True
    lights = line.split("[")[1].split("]")[0]
    positions = set([match.start() for match in re.finditer("#", lights)])
    button_not_found = True
    n_presses = 1
    while button_not_found and n_presses <= len(buttons):
        if try_k_buttons(set(), buttons, n_presses, positions, list()):
            total += n_presses
            button_not_found = False
        n_presses += 1
    if button_not_found:
        print("AAAAAA", line)
print(total)
# %%
import numpy as np
from scipy.optimize import linprog

total = 0
for iline, line in enumerate(data):
    print(iline)
    buttons = [
        list([int(x) for x in qq.split(")")[0].split(",")])
        for qq in line.split("(")[1:]
    ]
    jolts = np.array([int(x) for x in line.split("{")[1].split("}")[0].split(",")])
    newbuttons = np.array([np.zeros(len(jolts)) for _ in buttons])
    for ibutton, button in enumerate(buttons):
        for number in button:
            newbuttons[ibutton][number] = 1

    A_ub = -newbuttons.T
    b_ub = -jolts
    c = np.ones(A_ub.shape[1])
    result = linprog(c, A_eq=A_ub, b_eq=b_ub, integrality=1)
    total += np.sum(result.x)
print(total)
