import matplotlib.pyplot as plt

x_values = range(1,5_001)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
# Define Custom Colors
# ax.scatter(x_values, y_values,color='purple', s=10)

# Using a Colormap
ax.scatter(x_values, y_values,c=y_values, cmap=plt.cm.Blues, s=100)


# Set chart title label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of value", fontsize=14)

# ax.axis([0, 5_100, 0, 5_500_000])
# ax.ticklabel_format(style='plain')

# Set size of tick labels.
ax.tick_params(labelsize=10)

plt.show()


