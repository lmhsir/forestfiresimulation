import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib import colors
import time
import os

w_and_h_before_padding = 8  # width and height of the square array
forest = [["T" for x in range(w_and_h_before_padding)] for y in range(w_and_h_before_padding)]
f_array = np.array(forest)
f_array = np.pad(f_array, pad_width=1, mode='constant', constant_values=' ')

w_and_h = w_and_h_before_padding+2


adjacent_trees = ((-1,-1), (-1,0), (-1,1),
                  (0,-1),          (0, 1),
                  (1,-1),  (1,0),  (1,1))

regen_rate = 0.05
spread_rate = 0.8
spont_combust_rate = 0.01


def update_forest(old_array):
    new_list = [[' ' for x in range(w_and_h)] for y in range(w_and_h)]
    new_array = np.array(new_list)
    for x in range(w_and_h):
        for y in range(w_and_h):
            if old_array[x, y] == ' ':
                if 0 < x < 9 and 0 < y < 9:
                    if np.random.random() <= regen_rate:
                        new_array[x, y] = 'T'
                else:
                    new_array[x, y] = ' '
            elif old_array[x, y] == '#':
                new_array[x, y] = ' '
            elif old_array[x, y] == "T":
                for xb, yb in adjacent_trees:
                    if old_array[x+xb, y+yb] == '#':
                        if np.random.random() <= spread_rate:
                            new_array[x, y] = '#'
                        else:
                            new_array[x, y] = 'T'
                        break
                    else:
                        if np.random.random() <= spont_combust_rate:
                            new_array[x, y] = '#'
                        else:
                            new_array[x, y] = 'T'
    return new_array


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
delay = 0.1
while trees_remain:
    if time.time() >= prog_start + delay:
        f_array = update_forest(f_array)
        end_when_empty(f_array)
        print(f_array)
        print("\n")
        delay += 0.1
