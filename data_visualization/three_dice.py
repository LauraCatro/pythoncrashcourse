import plotly.express as px

from data_visualization.die_visual import dice_1
from dice import Dice

# Create a D6 and a D10
dice_1 = Dice(6)
dice_2 = Dice(6)
dice_3 = Dice(6)

# Make some rolls, and store results in a list.
# results = []
#for roll in range(1_000):
#    result = dice_1.roll() + dice_2.roll() + dice_3.roll()
#    results.append(result)

# List Comprehensions
results = [dice_1.roll() + dice_2.roll() + dice_3.roll() for roll in range(1_000)]

# Analyze the results.
max_results = dice_1.num_sides + dice_2.num_sides + dice_3.num_sides
poss_results = range(3, max_results+1)
frequencies = [results.count(value) for value in poss_results]

# Visualize the results.
title = "Results of Rolling a Three D6 1,000 Times"
labels = {'x':'Results', 'y':'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Further customize chart.
fig.update_layout(xaxis_dtick=1)

# fig.write_html('dice_visual_d6d10.html')
fig.show()