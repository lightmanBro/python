"Name: David Omotoso"
"week 5 Prove assignment on word game Part 1"


def main():


          print('Welcome buddy please input your name')
          name = input('Name: ')
          print(name + ' le\'ts Play a little funny game! are you in for the game? ')
          answer = input('Yes or No ')
          if answer.lower() == 'yes':
                    print('Bravo!! now roll your sleeves and lets get in the game.')
          elif answer.lower() == 'no':
                    print('its Okay buddy, i guess your\'re not in the mood for games')
                    exit()

          print(name + 'You are walking through a dark forest and find two items: a MATCH and a FLASHLIGHT. Which one do you want to pick up? ')

          choice1 = input('Match or Flashlight ')
          if choice1.lower() == 'match':
                    print(name + ' Wow good choice Match')
                    answer1 = input(name + ' You pick up the match and strike it, and for an instant, the forest around you is illuminated. You see a large grizzly bear, and then the match burns out. Do you want to RUN, or HIDE behind a tree? ')
                    if answer1.lower() == 'run':
                              print(name + ' you started running and just as you raised your head up you discoverd that you have ran into a.... ')
                    elif answer1.lower() == 'hide':
                              print(name + ' you were hiding and you discoverd that..... ')

          elif choice1.lower() == 'flashlight':
                    print(name + ' Wow good choice Flashlight')
                    choice2 = input(name + ' You pick up the flashlight and turn it on. You see the pathway lit up in front of you, but you thought you also heard something off to the side. Do you want to FOLLOW the path or LOOK in the trees for the thing that made the noise?... ')
                    if choice2.lower == 'follow':
                              print(name + ' you followed the path only to discover that...')
                    elif choice2.lower == 'look':
                              print(name + ' you looked at the direction of...... and..... ')
                              
          else: print(name + ' thanks i hope to talk to you later. ')

          restart = input( name + ' would you like to try again and make another choice? ')
          if restart.lower() == 'yes':
                    main()
          else:
                    exit()
main()