command = ''
started = False
while True:
    command = input('> ').lower()
    if command == 'start':
        if started:
            print('Car started already')
        else:
            started = True
            print('Car started...')
    elif command == 'stop':
        print(f'started {started}')
        if started == False:
            print('Car has not started...Car stopped already')
        else:
            started = False
            print('Car stopped')
    elif command == 'help':
        print('''
start - to start the car
stop - to stop the car
quit - to quit
        ''')
    elif command == 'quit':
        break
    else:
        print('Sorry, I don\'t understand that!')
