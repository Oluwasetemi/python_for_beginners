message = input('>')
words = message.split(' ')
emojis = {
    ":)": "😊",
    ":(": "😔"
}

output = ''
for ch in words:
    output += emojis.get(ch, ch) + ' '

print(output)
