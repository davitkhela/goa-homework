supported = ["lights off", 
             "lock the door", "open the door",
             "make coffee", "shut down"
            ]
command = input('Enter a supported command:')

if command in supported:
    print('OK')
else:
    print('Unknown')
