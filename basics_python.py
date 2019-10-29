'''Manipulation of list and data types and examples of some built in functions'''


# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]
del(second[1])
second = second + [9.50, 12.49]
second[2] = 12.50           #replace element
# Paste together first and second: full
full = first + second
print(full)
# Sort full in descending order: full_sorted
full_sorted = sorted(full, reverse = True)
full_copy = full[:] # explicit copy of list / alternatively list(full)
print(max(first))
print(len(first))


'''Everything is an object, examples of using methods on list and string'''

# string to experiment with: place
place = "poolhouse"

# Use upper() on place: place_up
place_up = place.upper()
# Print out the number of o's in place
print(place.count('o'))

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
# Print out the index of the element 20.0
print(areas.index(20))  
# Print out how often 9.50 appears in areas
print(areas.count(9.5))   
areas.append(24.5) # adds an element to the list it is called on
areas.append(15.45)
areas.remove(15.45)  # removes the first element of a list that matches the input

areas.reverse() # Reverse the orders of the elements in areas



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




'''Importing and using numpy array'''

# Import numpy
import numpy as np

# Create array from height_in with metric units: np_height_m
np_height_m = np.array(height_in) * 0.0254
# Create array from weight_lb with metric units: np_weight_kg
np_weight_kg = np.array(weight_lb) * 0.453592
# Calculate the BMI: bmi
bmi = np_weight_kg / np_height_m ** 2
# Print out bmi
print(bmi)

# Create the light array
light = bmi < 21
# Print out BMIs of all baseball players whose BMI is below 21
print(bmi[light])
print(len(bmi[light]))

results = np.array([True, 1, 2]) + np.array([3, 4, False]) # == np.array([4, 3, 0]) + np.array([0, 2, 2])

# Print out the weight at index 50
print(np_weight_lb[50])

# Print out sub-array of np_height_in: index 100 up to and including index 110
print(np_height_in[100:111])





'''Subsetting 2D numpy arrays'''
# regular list of lists
x = [["a", "b"], ["c", "d"]]
[x[0][0], x[1][0]]

# numpy
np_x = np.array(x)
np_x[:,0]
# Create np_baseball (2 cols)
np_baseball = np.array(baseball)
print(np_baseball.shape)
# Select the entire second column of np_baseball: np_weight_lb
np_weight_lb = np_baseball[:,1]
print(np_weight_lb)




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








