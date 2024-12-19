from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path('weather_data/sitka_weather_2021_full.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Printing the Headers and Their Positions.
for index, column_reader in enumerate(header_row):
    print(index, column_reader)

# Extract dates and high temperatures.
dates, prcps = [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    prc = float(row[5])
    dates.append(current_date)
    prcps.append(prc)

# Plot the high temperatures.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates,prcps, color='red')

# Format plot.
ax.set_title('Sitka Rainfall', fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Daily Rainfall amounts', fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
