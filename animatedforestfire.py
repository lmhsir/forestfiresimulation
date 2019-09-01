import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib import colors

Empty, Tree, Fire = 0, 1, 2  # This increases the readability of our code

# ---Generate forest array---
w_and_h_before_padding = 98  # width and height of the forest
forest = np.ones((w_and_h_before_padding, w_and_h_before_padding))  # generates a grid of Trees cells
f_array = np.array(forest)
f_array = np.pad(f_array, pad_width=1, mode='constant', constant_values=0)  # adds a boarder of Empty cells

w_and_h = w_and_h_before_padding+2  # width and height of forest + padding


# ---Neighbourhood of a cell---
adjacent_cells = ((-1,-1), (-1,0), (-1,1),
                   (0,-1),          (0,1),
                   (1,-1),  (1,0),  (1,1))

# ---Probabilities---
regen_rate = 0.08
spread_rate = 0.9
spont_combust_rate = 0.00008

# ---Update forest function---
# Rules:
# These rules are applied to every cell in the f_array for each iteration of the update_forest() function
# Any Tree cell has a spont_combust_rate probability of turning into a Fire cell
# For any Tree cell, each of it's adjacent_cells that is on Fire has a spread_rate probability of turning it into
# a Fire cell
# Any Fire cell will become an Empty cell
# Any Empty cell has a regen_rate probability of becoming a Tree cell


def update_forest(f_array):  # iterates through each cell in the f_array and updates the cell according to the Rules
    new_array = np.zeros((w_and_h, w_and_h))
    for x in range(w_and_h):
        for y in range(w_and_h):
            if f_array[x, y] == Empty:
                if 0 < x < 99 and 0 < y < 99:  # if current cell part of forest (and not the padding)
                    if np.random.random() <= regen_rate:
                        new_array[x, y] = Tree
                else:
                    new_array[x, y] = Empty
            elif f_array[x, y] == Fire:
                new_array[x, y] = Empty
            elif f_array[x, y] == Tree:
                for xb, yb in adjacent_cells:
                    if f_array[x+xb, y+yb] == Fire:  # if any adjacent cells = Fire
                        if np.random.random() <= spread_rate:
                            new_array[x, y] = Fire
                        else:
                            new_array[x, y] = Tree
                        break
                    else:
                        if np.random.random() <= spont_combust_rate:
                            new_array[x, y] = Fire
                        else:
                            new_array[x, y] = Tree
    return new_array


# ---Map desired colours to the values in our forest---
colour_list = ['black', 'forestgreen', 'white', 'darkorange']
colour_map = colors.ListedColormap(colors=colour_list)  # make a colour map from a list of colours
bounds = [0, 1, 2, 3]
normalised_data = colors.BoundaryNorm(boundaries=bounds, ncolors=colour_map.N)  # make colormap index based on integers

# ---Plot and display the figure---
fig = plt.figure(figsize=(5, 5))  # plots a figure
ax = fig.add_subplot(1, 1, 1)  # plot a 1x1 grid on the first subplot
ax.set_axis_off()  # turns off the x and y axis for the grid
im = ax.imshow(f_array, cmap=colour_map, norm=normalised_data)  # display an image of our forest array with colours
                                                                # mapped to the normalised data


# ---Animate function---
def animate(x):  # this function is repeatedly called by the FuncAnimation() function to create each frame of animation
    im.set_data(animate.f_array)  # sets the x and y data from the forest array
    animate.f_array = update_forest(animate.f_array)  # updates the forest array


animate.f_array = f_array  # this binds our forest array to the identifier f_array in the animate functions namespace

interval = 16  # set the ms time interval between frames of animation
anim = animation.FuncAnimation(fig=fig, func=animate, interval=interval)  # makes the animation by repeatedly calling
                                                                          # animate() function

plt.show()  # shows the animated figure
