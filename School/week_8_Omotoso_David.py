
secret_word = 'Moroni'
userGuess = ''
guessCount = 0
guess_limit = 3
hint = 'The secret word starts with M and ends with i'
out_of_guesses = False
while userGuess != secret_word and not(out_of_guesses):
          if guessCount < guess_limit:
                    userGuess = input('Enter guess: ')
                    guessCount += 1
                    secretWord = len(secret_word)
                    guessTime = len(userGuess)
                    print(f'your guess is {userGuess.upper()}, it has {guessTime} letters and the Secret Word has {secretWord} letters\n')
                    print(hint)
                    
                    if guessCount == guess_limit:
                              print('Out of guesses')

                    elif userGuess == secret_word.lower():
                              print(f'Your guess is {userGuess.upper()} and the secret word is {secret_word.upper()}')
                              print('Bravo! You win')
                              exit()   
                    else:
                               print(f'you have {-guessCount} guesses remaining out of 3')
                      
          else:
                    out_of_guesses = True

if out_of_guesses and guessCount == guess_limit:
          print('Sorry Buddy, YOU LOSE')