with open("data\day1_data.txt") as file:
    data = file.read()

########################################################
########################################################
# ------------------------Part 1------------------------
# Find the Elf carrying the most Calories.
# How many total Calories is that Elf carrying?
# ------------------------Part 1------------------------

def get_highest_calories(data):
    highest_calories = 0
    current_elf_calories = 0
    rows = data.split('\n')
    for row in rows:
        if(row):
            current_elf_calories += int(row)
        if not (row):
            if(highest_calories < current_elf_calories):
                highest_calories = current_elf_calories
            current_elf_calories = 0 
    return highest_calories
# ------------------------------------------------------
# -------------------- answer = 68923-------------------

########################################################
########################################################

# ------------------------Part 2------------------------
# Find the top three Elves carrying the most Calories.
# How many Calories are those Elves carrying in total?
# ------------------------Part 2------------------------

def get_highest_calories(data):
    top_3_highest_calories = [0, 0, 0]
    total_calories = 0
    current_elf_calories = 0
    rows = data.split('\n')
    for row in rows:
        if(row):
            current_elf_calories += int(row)
        if not (row):
            if(current_elf_calories > min(top_3_highest_calories)):
                index = top_3_highest_calories.index(min(top_3_highest_calories))
                top_3_highest_calories[index] = current_elf_calories
            current_elf_calories = 0 

    for n in top_3_highest_calories:
        total_calories += n
    return total_calories

print(get_highest_calories(data))

# ------------------------------------------------------
# -------------------- answer = 200044------------------

