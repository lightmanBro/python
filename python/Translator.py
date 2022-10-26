from cmath import phase


def translate(phrase):
          translation = ''
          for letter in phrase:
                    if letter.lower() in 'aeiou':
                              if letter.isupper():
                                        translation = translation + 'G'
                              else:
                                         translation = translation + 'g'
                    else:
                              translation = translation + letter
          return translation

phrase = input('Enter a phrase: '.upper())
print(translate(phrase))
 