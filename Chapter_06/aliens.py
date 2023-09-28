aline_0 = {'color':'green','points':5}
aline_1 = {'color':'yellow','points':10}
aline_2 = {'color':'red','points':15}

aliens = [aline_0,aline_1,aline_2]

for alien in aliens:
    print(alien)

aliens = []

for alien_number in range(0,30):
    new_alien = {'color':'green',
                 'points':5,
                 'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

for alien in aliens[:5]:
    print(alien)

print("......")

print("Total number of aliens: " + str(len(aliens)))
