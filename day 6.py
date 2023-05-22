with open("data\day6_data.txt") as file:
    data = file.read()

########################################################
########################################################
# ------------------------Part 1------------------------
# How many characters need to be processed before
# the first start-of-packet?
# ------------------------Part 1------------------------

def get_characters_amount(data):
    outer_i = 0
    while outer_i < len(data):
        inner_i = 0
        s = set({})
        s.add(data[inner_i + outer_i])
        s.add(data[inner_i + outer_i + 1])
        s.add(data[inner_i + outer_i + 2])
        s.add(data[inner_i + outer_i + 3])

        if len(s) == 4:
            correct = '1'
            return outer_i + 4

        outer_i += 1

    return 0

# ------------------------------------------------------
# ------------------- answer = 1262 --------------------

########################################################
########################################################

# ------------------------Part 2------------------------
# How many characters need to be processed before
# the first start-of-message marker is detected?
# ------------------------Part 2------------------------

def get_characters_amount_part_two(data):
    outer_i = 0
    while outer_i < len(data):
        inner_i = 0
        s = set({})

        for c in range(14):
            s.add(data[inner_i + outer_i + c])
            

        if len(s) == 14:
            correct = '1'
            return outer_i + 14

        outer_i += 1

    return 0

print(str(get_characters_amount_part_two(data)))

# ------------------------------------------------------
# ------------------- answer = 3444 --------------------