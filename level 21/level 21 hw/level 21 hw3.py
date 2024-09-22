alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
         'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
         'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
        ]
n1 = int(input('Enter a number 0-25:'))
n2 = int(input('Enter a number 0-25:'))
n3 = int(input('Enter a number 0-25:'))

print(alpha[n1])
print(alpha[n2])
print(alpha[n3])

if 25 < n1:
    print('Number too high!')

elif 25 < n2:
    print('Number too high!')

elif 25 < n3:
    print('Number too high!')
