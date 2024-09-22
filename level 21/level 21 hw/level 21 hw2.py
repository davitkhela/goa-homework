day = int(input('Enter a day(as a number, ex monday is 1 and etc:)'))
hour = int(input('Enter an hour:'))

if day < 6 and 10 < hour < 21:
    print('Open')
else:
    print('Closed')