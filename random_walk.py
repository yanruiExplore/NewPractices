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