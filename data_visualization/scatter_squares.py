import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
# Define Custom Colors
# ax.scatter(x_values, y_values,color='purple', s=10)

# Using a Colormap
ax.scatter(x_values, y_values,c=y_values, cmap=plt.cm.Greens, s=10)


# Set chart title label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of value", fontsize=14)

# Set the range for each axis
ax.axis([0, 1100, 0, 1_100_000])
ax.ticklabel_format(style='plain')

# Set size of tick labels.
ax.tick_params(labelsize=14)

# plt.show()

# Saving your Plots Automatically
plt.savefig("squares_plot.png", bbox_inches='tight')
