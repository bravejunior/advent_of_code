with open("data\day4_data.txt") as file:
    data = file.read()

########################################################
########################################################
# ------------------------Part 1------------------------
# In how many assignment pairs does one range fully
# contain the other?
# ------------------------Part 1------------------------


def print_pairs_with_covered_range(data):
    rows = data.split('\n')
    amount_of_pairs = 0

    for row in rows:
        pair = row.split(',')
        first_elf_range = pair[0].split('-')
        first_elf_from = first_elf_range[0]
        first_elf_to = first_elf_range[1]

        second_elf_range = pair[1].split('-')
        second_elf_from = second_elf_range[0]
        second_elf_to = second_elf_range[1]

        if first_elf_from <= second_elf_from:
            if first_elf_to >= second_elf_to:
                amount_of_pairs += 1

        elif second_elf_from <= first_elf_from:
            if second_elf_to >= first_elf_to:
                amount_of_pairs += 1

    print(str(amount_of_pairs))

    # print('',amount_of_pairs)

# ------------------------------------------------------
# -------------------- answer = 483 --------------------

########################################################
########################################################

# ------------------------Part 2------------------------
# def print_pairs_with_covered_range(data):

# each three-Elf group. What is the sum of the priorities
# of those item types?
# ------------------------Part 2------------------------


def print_pairs_with_covered_range_part_two(data):
    rows = data.split('\n')
    amount_of_pairs = 0

    for row in rows:
        pair = row.split(',')
        is_contained = False
        first_elf_from_to = pair[0].split('-')
        first_elf_from = int(first_elf_from_to[0])
        first_elf_to = int(first_elf_from_to[1]) + 1

        second_elf_from_to = pair[1].split('-')
        second_elf_from = int(second_elf_from_to[0])
        second_elf_to = int(second_elf_from_to[1]) + 1

        first_elf_range = range(first_elf_from, first_elf_to)
        second_elf_range = range(second_elf_from, second_elf_to)

        duplicates_found = bool(set(first_elf_from_to)
                                & set(second_elf_from_to))

        if not duplicates_found:
            for i in first_elf_range:
                if i in second_elf_range:
                    is_contained = True
                    break

        if duplicates_found or is_contained:
            amount_of_pairs += 1

    print(str(amount_of_pairs))


print_pairs_with_covered_range_part_two(data)

# ------------------------------------------------------
# -------------------- answer = 874 -------------------
