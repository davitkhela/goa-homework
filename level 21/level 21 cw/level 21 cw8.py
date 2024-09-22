wins = input('Please enter a valid amount of wins: ')
ties = input('Please enter a valid amount of ties: ')

wins = int(wins)
ties = int(ties)
tie_points = (ties//2)

points = (wins+tie_points)
print('Your points:',points)