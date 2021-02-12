num = input('Enter the number? ')
num_in_words = {'1': 'One', '2': 'Two', '3': 'Three'}

output = ''
for ch in num:
    output += num_in_words.get(ch, '!') + ' '

print(output)
