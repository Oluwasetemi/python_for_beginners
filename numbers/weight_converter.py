weight = int(input('Weight: '))
unit = input('(L)bs or (K)g: ')

if unit.upper() == 'L' or unit.lower() == 'l':
    converted = weight * .45
    print(f'You are {converted} kilos')
elif unit.upper() == 'K' or unit.lower() == 'k':
    converted = weight / .45
    print(f'You are {converted} pounds')
