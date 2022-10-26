
word = 'commitment'
favouriteLetter = input('what is your Favourite Letter? ')

for letter in word:
          if letter.lower() == favouriteLetter.lower():
                    print(letter.upper(), end='')
          else:
                    print(letter.lower(), end='')