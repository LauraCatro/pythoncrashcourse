# Make an empty list for storing aliens
aliens = []

# Make 30 green aliens
for alien in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
    elif alien['color'] == 'yelow':
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'

# Show the firts 5 aliens

for alien in aliens[:5]:
    print(alien)

print("...")

# Show how many aliens have been created
print(f"Total number of aliens: {len(aliens)}")
