import string
with open("day3_data.txt") as file:
    data = file.read()

################### a-z =  1-26p ###############
################### A-Z = 27-52p ###############
# --------------------Part 1--------------------

def get_priority_of_character(character):
    character_points_given = {}
    points = 1

    for i in string.ascii_lowercase:
        character_points_given[i] = points
        points += 1

    for i in string.ascii_uppercase:
        character_points_given[i] = points
        points += 1

    return character_points_given[character]

def get_sum_of_priorities(data):
    rows = data.split('\n')
    total_sum = 0
    for row in rows:
        character_array = []
        left_compartment = []
        right_compartment = []
        index = 0

        for i in row:
            character_array.append(i)

        for i in character_array:
            if index+1 <= (len(character_array) // 2):
                left_compartment.append(i)
                index += 1
            else:
                right_compartment.append(i)
                index += 1

        for i in left_compartment:
            if i in right_compartment:
                total_sum += get_priority_of_character(i)
                break
    return total_sum

# ----------------------------------------------
# ---------------- answer = 7889 ---------------

################################################
################################################

# --------------------Part 2--------------------
# ----------------------------------------------

def get_sum_of_priorities_part_two(data):
    rows = data.split('\n')
    total_sum = 0
    members = 0
    index = 0
    group_member_arr = []

    while (index < len(rows)):
        if members >= 3:
            members = 0
            group_member_arr = []
        members += 1

        character_array = []
        for i in rows[index]:
            character_array.append(i)
        group_member_arr.append(character_array)
        index += 1

        if (members >= 3):
            arr1 = group_member_arr[0]
            arr2 = group_member_arr[1]
            arr3 = group_member_arr[2]

            common_character = str(find_common_character(arr1, arr2, arr3))

            total_sum += get_priority_of_character(common_character)
    
    return total_sum

def find_common_character(arr1, arr2, arr3):
    common_elements = ''

    for i in arr1:
        if (i in arr2 and i in arr3):
            common_elements = i
            break
    return common_elements

print(get_sum_of_priorities_part_two(data))

# ----------------------------------------------
# ---------------- answer = 2825 ---------------