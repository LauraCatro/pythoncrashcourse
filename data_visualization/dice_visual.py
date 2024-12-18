import plotly.express as px
from dice import Dice

# Create a D6
dice = Dice()

# Make some rolls, and store results in a list.
results = []
for roll in range(1000):
    result = dice.roll()
    results.append(result)

# Analyze the results.
frequencies = []
poss_results = range(1, dice.num_sides + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
fig = px.bar(x=poss_results, y=frequencies)
fig.show()