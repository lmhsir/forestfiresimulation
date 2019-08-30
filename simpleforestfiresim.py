import numpy as np
import time

w_and_h_before_padding = 8  # width and height of the square array
forest = [["T" for x in range(w_and_h_before_padding)] for y in range(w_and_h_before_padding)]
f_array = np.array(forest)
f_array = np.pad(f_array, pad_width=1, mode='constant', constant_values=' ')

w_and_h = w_and_h_before_padding+2

f_array[np.random.randint(1, w_and_h-1), np.random.randint(1,w_and_h-1)] = "#"


adjacent_trees = ((-1,-1), (-1,0), (-1,1),
                  (0,-1),          (0, 1),
                  (1,-1),  (1,0),  (1,1))


def update_forest(old_array):
    new_array = {}
    for x in range(w_and_h):
        for y in range(w_and_h):
            if old_array[x, y] == ' ':
                new_array[x, y] = ' '
            elif old_array[x, y] == '#':
                new_array[x, y] = ' '
            elif old_array[x, y] == "T":
                for xb, yb in adjacent_trees:
                    if old_array[x+xb, y+yb] == '#':
                        if np.random.random() <= 0.7:
                            new_array[x, y] = '#'
                        else:
                            new_array[x, y] = 'T'
                        break
                    else:
                        if np.random.random() <= 0.3:
                            new_array[x, y] = '#'
                        else:
                            new_array[x, y] = 'T'
    return new_array


def generate_empty_array(length):
    empty_list = []
    for i in range(length):
        row = []
        for i in range(length):
            row.append(" ")
        empty_list.append(row)
    empty_array = np.array(empty_list)
    return empty_array


def fill_array(dictionary, empty_array):
    for key, value in dictionary.items():
        empty_array[key] = value
    return empty_array


def end_when_empty(array):
    value = 0
    for x in range(w_and_h):
        for y in range(w_and_h):
            if array[x, y] == ' ':
                value += 0
            else:
                value += 1
    if value == 0:
        print("\nThe forest burnt down :(")
        quit()


trees_remain = True

print(f_array)
print("\n")

prog_start = time.time()
delay = 0.5
while trees_remain:
    if time.time() >= prog_start + delay:
        f_dictionary = update_forest(f_array)
        blank_array = generate_empty_array(w_and_h)
        f_array = fill_array(f_dictionary, blank_array)
        end_when_empty(f_array)

        print(f_array)
        print("\n")
        delay += 0.5