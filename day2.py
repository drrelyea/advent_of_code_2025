# %%

from utils import load_advent_of_code

data = load_advent_of_code(202502)

print(data)


# %%
def get_eliminate_total(low, hi):
    total = 0
    number_low_digits = len(low)
    number_hi_digits = len(hi)
    repeated_numbers = set()
    for digit_length in range(number_low_digits, number_hi_digits + 1):
        if digit_length // 2 == digit_length / 2:
            if number_low_digits == number_hi_digits:
                first_part_low = int(low[0 : digit_length // 2])
                second_part_low = int(low[digit_length // 2 :])
                if second_part_low > first_part_low:
                    first_part_low += 1
                first_part_hi = int(hi[0 : digit_length // 2])
                second_part_hi = int(hi[digit_length // 2 :])
                if second_part_hi >= first_part_hi:
                    first_part_hi += 1
                for prefix in range(first_part_low, first_part_hi):
                    # total += int(str(prefix) + str(prefix))
                    the_number_I_want = int(str(prefix) + str(prefix))
                    repeated_numbers.add(the_number_I_want)
                    total += the_number_I_want
            elif digit_length == number_low_digits:
                first_part = int(low[0 : digit_length // 2])
                second_part = int(low[digit_length // 2 :])
                if second_part > first_part:
                    first_part += 1
                for prefix in range(first_part, 10 ** (digit_length // 2)):
                    # total += int(str(prefix) + str(prefix))
                    the_number_I_want = int(str(prefix) + str(prefix))
                    repeated_numbers.add(the_number_I_want)
                    total += the_number_I_want
            elif digit_length == number_hi_digits:
                first_part = int(hi[0 : digit_length // 2])
                second_part = int(hi[digit_length // 2 :])
                if second_part >= first_part:
                    first_part += 1
                for prefix in range(10 ** (digit_length // 2 - 1), first_part):
                    # total += int(str(prefix) + str(prefix))
                    the_number_I_want = int(str(prefix) + str(prefix))
                    repeated_numbers.add(the_number_I_want)
                    total += the_number_I_want
            else:
                for prefix in range(
                    10 ** (digit_length // 2 - 1), 10 ** (digit_length // 2)
                ):
                    the_number_I_want = int(str(prefix) + str(prefix))
                    repeated_numbers.add(the_number_I_want)
                    total += the_number_I_want
    print(len(repeated_numbers))
    return sum(repeated_numbers)


ranges = data[0].split(",")
eliminate_total = 0
for therange in ranges:
    low, hi = therange.split("-")
    newtotal = get_eliminate_total(low, hi)
    print(low, hi, newtotal)
    eliminate_total += newtotal
print(eliminate_total)


# %%


def get_multidupe_total(low, hi):
    number_low_digits = len(low)
    number_hi_digits = len(hi)
    lowint = int(low)
    hiint = int(hi)
    repeated_numbers = set()
    for digit_length in range(max(number_low_digits, 2), number_hi_digits + 1):
        for dupe_length in range(1, number_hi_digits):
            # for dupe_length in range(
            #     math.ceil(digit_length / 2), math.ceil(digit_length / 2 + 1)
            # ):
            if digit_length // dupe_length == digit_length / dupe_length:
                ndupes = digit_length // dupe_length
                if ndupes == 1:
                    continue
                minnum = 10 ** (dupe_length - 1)
                maxnum = 10**dupe_length
                for repeated_number in range(minnum, maxnum):
                    the_number_I_want = int(str(repeated_number) * ndupes)
                    if lowint <= the_number_I_want <= hiint:
                        repeated_numbers.add(the_number_I_want)
    print(len(repeated_numbers))
    # print(repeated_numbers)
    return sum(repeated_numbers)


ranges = data[0].split(",")
eliminate_total = 0
for therange in ranges:
    low, hi = therange.split("-")
    newtotal = get_multidupe_total(low, hi)
    print(low, hi, newtotal)
    eliminate_total += newtotal
print(eliminate_total)

# %%
