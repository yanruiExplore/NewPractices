'''Practices using numpy and matplotlib.pyplot packages'''


''' Simulating the random walk to calculate the distribution and probability of reaching 60 steps based on the distribution
calculated
Rules:
Can't go lower than step 0
0.1% chance of falling down the stairs, which means start from step 0
'''

import numpy as np 
import matplotlib.pyplot as plt
np.random.seed(123)

#simulate random walk 500 times
all_walks = []

for i in range(500):
    random_walk = [0]
    for x in range(100):
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step-1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        if np.random.rand() <= 0.001:
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)

print(np.array(all_walks))
np_aw_t = np.transpose(np.array(all_walks))
print(np_aw_t.shape)

#select last row from np_aw_t : ends
ends = np_aw_t[-1,:]
print(ends)

#plot histogram of ends, display plot

plt.hist(ends)
plt.show()

'''
Calculating the probability of reaching 60 or greater number of steps
'''
print(len(ends[ends>=60])/500)





'''Importing and using the maths module'''

import math
# Definition of radius
r = 0.43
# Calculate C
C = 2 * math.pi * r
# Calculate A
A = math.pi * r ** 2
# Build printout
print("Circumference: " + str(C))
print("Area: " + str(A))

# Travel distance of Moon over 12 degrees. Assuming spherical orbit
# Definition of radius
r = 192500
phi = math.radians(12)
dist = r * phi





'''Working with matrices using numpy arrays'''

# Create np_baseball (3 cols) representing height (in inches), weight (in pounds) and age (in years)
np_baseball = np.array(baseball)
# Create numpy array: conversion to convert the units of height and weight to metric (meters and kilograms respectively)
conversion = np.array([0.0254, 0.453592, 1])
# Print out product of np_baseball and conversion
print(np_baseball * conversion)
np_mat = np.array([[1, 2],[3, 4],[5, 6]])
np_mat * 2
np_mat + np.array([10, 10])
np_mat + np_mat



'''Working with numpy statistics to know your data'''

# Create np_height_in from np_baseball
np_height_in = np_baseball[:,0]
# Print out the mean of np_height_in
print(np.mean(np_height_in))
# Print out the median of np_height_in
print(np.median(np_height_in))
# Print out the standard deviation on height.
stddev = np.std(np_baseball[:,0])
# Print out correlation between first and second column. 
corr = np.corrcoef(np_baseball[:,0], np_baseball[:,1])
print("Correlation: " + str(corr))




'''Hypothesis: the median height of goalkeepers is higher than that of other players on the soccer field'''
# Convert positions and heights to numpy arrays: np_positions, np_heights
np_positions = np.array(positions)
np_heights = np.array(heights)
# Heights of the goalkeepers: gk_heights
gk_heights = np_heights[np_positions == 'GK']
# Heights of the other players: other_heights
other_heights = np_heights[np_positions != 'GK']
# Print out the median height of goalkeepers. Replace 'None'
print("Median height of goalkeepers: " + str(np.median(gk_heights)))

# Print out the median height of other players. Replace 'None'
print("Median height of other players: " + str(np.median(other_heights)))

print(np.median(gk_heights) > np.median(other_heights))




'''Generating random list of data'''

new_height = np.round(np.random.normal(1.75, 0.20, 5000),2)
new_weight = np.round(np.random.normal(60.32, 15, 5000), 2)
np_city = np.column_stack((new_height, new_weight))


'''An important function for use as a timestamp'''
import time
print(time.asctime())
# the asctime function returns the current time of the systme as a string





