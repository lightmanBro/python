print()
trials = 1
while trials <= 2:
          guess = 'moroni'
          print('Welcome to the word guessing game\n')
          print('Your hint is _ _ _ _ _')
          guessWord = input('what is your guess? ')
          hint = print(f'your hint is {guessWord.upper()}')
          while guessWord  != 'moroni' :
                    guessWord = input('What is your guess ')
                    secretWord = len(guess)
                    guessTime = len(guessWord)
                    print(f'your guess has {guessTime} letters and the Secret Word has {secretWord} letters\n')
                    if guessWord != guess:
                              print('guess is not correct\n Please try again')
                              if 'm' in guessWord[0].lower():
                                        print(f'Your Hint is {guessWord[0].capitalize()} _ _ _ _ ')
                              elif 'm' not in guessWord[0].lower() and 'm' in guessWord:
                                        print(f'Your Hint is {guess[0].lower()} _ _ _ _ \n')
                              if 'o' in guessWord[1].lower():
                                        print(f'Your Hint is _ {guess[1].upper()} _ {guess[1].upper()} _ _ \n')
                              elif 'o' not in guessWord[1] and 'o' in guessWord:
                                        print(f'Your Hint is _ {guess[1].lower()} _ {guess[1].lower()} _ _ \n')
                              if 'r' in guessWord[2].lower():
                                        print(f'Your Hint is _ _ {guess[2].upper()} _ _ _\n')
                              elif 'r' not in guessWord[2].lower() and 'r' in guessWord:
                                        print(f'Your Hint is _ _ {guess[2].lower()} _ _ _\n')
                              if 'n' in guessWord.lower():
                                        print(f'Your Hint is _ _ _ _ {guess[4].upper()}  _ \n')
                              elif 'n' not in guessWord and 'n' in guessWord:
                                        print(f'Your Hint is _ _ _ _ {guess[4].lower()}  _ \n')
                              if 'i' in guessWord.lower():
                                        print(f'Your hint is _ _ _ _ _ {guess[5].upper()}\n')
                              elif 'i' not in guessWord and 'i' in guessWord:
                                        print(f'Your hint is _ _ _ _ _ {guess[5].lower()}\n')
          print(' guess is correct '.upper() + guessWord.upper() )
print(f' you have used {trials} out of your guess chances')
trials = trials + 1
if trials == 3:
          exit()
