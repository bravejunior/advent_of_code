with open("day2_data.txt") as file:
    data = file.read()

########################################################
########################################################
# ------------------------Part 1------------------------
# What would your total score be if everything
# goes exactly according to your strategy guide?
# ------------------------Part 1------------------------

def r_p_s(data):
    total_score = 0
    round_score = 0
    rounds = data.split('\n')
    for round in rounds:
        if round:
            round_score = 0
            key, value = round.split(' ')
            if value == 'X':
                round_score += 1
                if key == 'A':
                    round_score += 3
                elif key == 'C':
                    round_score += 6
            if value == 'Y':
                round_score += 2
                if key == 'B':
                    round_score += 3
                elif key == 'A':
                    round_score += 6
            if value == 'Z':
                round_score += 3
                if key == 'B':
                    round_score += 6
                elif key == 'C':
                    round_score += 3
            total_score += round_score
    return total_score
# ------------------------------------------------------
# -------------------- answer = 9177--------------------

########################################################
########################################################

# ------------------------Part 2------------------------
# Following the Elf's instructions for the second column
# what would your total score be if everything goes
# exactly according to your strategy guide?
# ------------------------Part 2------------------------

def get_points(key, value):
    lose_against = {'A': 3, 'B': 1, 'C': 2}
    win_against = {'A': 8, 'B': 9, 'C': 7}
    draw_against = {'A': 4, 'B': 5, 'C': 6}

    if value == 'X':
        return lose_against[key] 
    if value == 'Y':
        return draw_against[key] 
    if value == 'Z':
        return win_against[key]     
    return 0

def r_p_s_new(data):
    total_score = 0
    rounds = data.split('\n')
    for round in rounds:
        if round:
            key, value = round.split(' ')
            points = get_points(key, value)

            total_score += points
    return total_score

print(r_p_s_new(data))

# ------------------------------------------------------
# -------------------- answer = 12111-------------------
    