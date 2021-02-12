first_name = 'Oluwasetemi'
last_name = 'Stephen'
message = first_name + ' ' + last_name + ' is a python developer'
formatted_message = f'{first_name} {last_name} is a python developer'
print(len(formatted_message))
print(formatted_message.find('o'))
print('python' in formatted_message)
formatted_message_clone = formatted_message[:11]
""" print(formatted_message_clone.upper())
print(formatted_message_clone.lower())
print(list(formatted_message_clone))
print(tuple(formatted_message_clone))
print(bool(formatted_message_clone)) """

# find and replace
str_message = 'Python for beginners'
new_message = str_message.replace('beginners', 'absolute beginners')
print(new_message)
