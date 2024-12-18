import matplotlib.pyplot as plt
from random_walk import RandomWalk
#from matplotlib import colormaps
#print(colormaps)

rw = RandomWalk()
rw.fill_walk()

# Plot the points in the walk.
plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, c=rw.y_values, cmap=plt.cm.Spectral, s=15)
ax.set_aspect('equal')
plt.show()
