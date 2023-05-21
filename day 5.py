import re

with open("data\day5_data.txt") as file:
    data = file.read()

########################################################
########################################################
# ------------------------Part 1------------------------
# After the rearrangement procedure completes,
# what crate ends up on top of each stack?
# ------------------------Part 1------------------------

def get_stacks(data):
    box_column_position = {}
    cd = str(data.split('move')[0])
    ca = cd.split('\n')
    ca.pop(10)
    ca.pop(9)
    ca.pop(8)
    column = 0
    row = 0
    position = len(ca) +1

    for row in ca:
        position -= 1
        column = 0
        characters_left = len(row) - 1
        box_start = 0
        box_end = 3



        while characters_left >= 0:
            if row[1:2] != 1 or row[1:2] != '\n':
                column += 1
                box = row[box_start:box_end]

                if box.isspace():
                    box = 'NONE'

                box_start += 4
                box_end += 4
                characters_left -= 4
                s_column = str(str(column))

                if s_column in box_column_position:
                    # If the key exists, append to the existing array
                    box_column_position[s_column].append(box)
                else:
                    # If the key doesn't exist, create a new array with the element
                    box_column_position[s_column] = [box]


        for i in box_column_position:
            arr = box_column_position[i]
            for a in arr:
                if a == 'NONE':
                    box_column_position[i].remove(a)


    for i in box_column_position:
        arr = box_column_position[i]
        arr.reverse()
        box_column_position[i] = arr

            # add boxes
        
    return box_column_position

def get_order(data):
    b = data.split('\n')
    i = 0
    while 9 >= i:
        b.pop(0)
        i += 1
    return b

def get_crates_on_top(data):
    stacks = get_stacks(data)

    order = get_order(data)

    for o in order:
        parts = o.split()
        num_to_move = int(parts[1])
        source_stack = parts[3]
        destination_stack = parts[5]
        for n in range(int(num_to_move)):
            stack_from = stacks[str(source_stack)]
            box = stack_from.pop()
            stacks[str(destination_stack)].append(box)

    top_boxes = []

    for i in stacks:
        arr = stacks[i]
        top_boxes.append(arr.pop())

    return top_boxes

print(get_crates_on_top(data))

# ------------------------------------------------------
# ----------------- answer = DHBJQJCCW -----------------

########################################################
########################################################

# ------------------------Part 2------------------------
# After the rearrangement procedure completes,
# what crate ends up on top of each stack?
# ------------------------Part 2------------------------