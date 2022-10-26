'''
using Dictionary to map a characters to emoji
using the .split('') method to split words in a sentence into different strings
'''
message = input('> ')
words = message.split(' ')
emojis = {
          ':)': '😁',
          ':(': '😞',
          'happiness':'😀'
}
output = ''
for word in words:
          output += emojis.get(word, word) + ' '
print(output)