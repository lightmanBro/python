'''
Name: Omotoso David
Title: Week 9 & 10 assignment on creating a shopping app.
Comment: Everything here is my work,  not copied from the internet or any other sources.
'''
print('     Welcome to our store\n Buy quality goods at affordable Prices')
options = int(input(' Enter 1 to add a new items to your Cart.\n Enter 2 to display the items in your shopping cart.\n Enter 3 to remove an item from your shopping cart.\n Enter 4 to calculate the items in your cart.\n Enter 5 to Quit.\n Enter a number: '))

itemList = []
itemPrices = []
totalCount = 0
enteredCount = 3
while itemList != '':
          if options == 1:
                    if totalCount < enteredCount:
                              itemList.append(input('Add Item: '))
                              itemPrices.append(int(input('Amount: $')))
                              totalCount += 1
                    elif totalCount == enteredCount:
                              check = int(input('Enter 2 to check the items in your cart or 1 to continue shopping '))
                              if check == 2:
                                        print('\nYou Have....')
                                        print('------------------')
                                        for i in range(len(itemList)):
                                                  print(f'{i}.{itemList[i]} - ${itemPrices[i]}\n')
                                                  
                                        calc = int(input('Enter 1 to continue shopping\n,Enter 3 to remove items by index number 0 1 2 3....\n,Enter 4 to calculate the total costs of the items in your list.  '))

                                        if calc == 3:
                                                for items in range(len(itemList and itemPrices)):
                                                      items.pop(int(input('Enter the index number of the items you want to remove: ')))
                                                #   itemList.pop(int(input(f'{itemList} {itemPrices} Please remove the items by its index number:')))
                                                # #   itemPrices.pop(int(input('Please remove the price of the item: ')))
                                                print('You now have in your Cart,')
                                                for i in range(len(itemList)):
                                                      print(f'{i+1}.{itemList[i]} - ${itemPrices[i]}\n')
                                        elif calc == 1:
                                                  itemList.append(input('Add Item: '))
                                                  itemPrices.append(int(input('Amount: $')))

                                        elif calc == 4:
                                                  print('The cost of the items in your cart is $',sum(itemPrices))
                                                  done = int(input('Enter 5 to checkout\n Enter 1 to return to continue shopping.\n Enter:  '))
                                                  if done == 5:
                                                            print('Thank you for Shopping with us')
                                                            exit()
                                                  elif done == 1:
                                                            itemList.append(input('Add Item: '))
                                                            itemPrices.append(int(input('Amount: $')))       
                              elif check == 1:

                                    
                                        itemList.append(input('Add Item: '))
                                        itemPrices.append(int(input('Amount: $')))
          elif options == 2:
                    print('You selected Option 2 but your list is empty at the moment')
                    options = int(input(' Enter 1 to add a new items to your Cart.\n Enter 2 to display the contents of your shopping cart.\n Enter 3 to remove an item from your shopping cart.\n Enter 4 to calculate the items in your cart.\n Enter 5 to Quit.\n Enter a number: '))

          elif options == 3:
                    print('Your list is empty at the moment Please select option 1 to add items to your list.')
                    options = int(input(' Enter 1 to add a new items to your Cart.\n Enter 2 to display the contents of your shopping cart.\n Enter 3 to remove an item from your shopping cart.\n Enter 4 to calculate the items in your cart.\n Enter 5 to Quit.\n Enter a number: '))

          elif options == 4:
                    print('Your List is empty at the moment, Please select Option 1 to add items to the list\n so that you can cslculate your total')
                    options = int(input(' Enter 1 to add a new items to your Cart.\n Enter 2 to display the contents of your shopping cart.\n Enter 3 to remove an item from your shopping cart.\n Enter 4 to calculate the items in your cart.\n Enter 5 to Quit.\n Enter a number: '))

          elif options == 5:
                    end = input('You have no items in your cart at the moment,\n nevertheless you can quit if you want to\n Enter Yes / No ')
                    if end.lower() == 'yes':
                              print('Thank you so much for checking by.\n We hope to serve you better whenever you check by later. ')
                              quit()
                    elif end.lower() == 'no':
                              options = int(input(' Enter 1 to add a new items to your Cart.\n Enter 2 to display the contents of your shopping cart.\n Enter 3 to remove an item from your shopping cart.\n Enter 4 to calculate the items in your cart.\n Enter 5 to Quit.\n Enter a number: '))
'''
end of the programme
'''