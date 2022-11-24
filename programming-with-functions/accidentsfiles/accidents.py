import csv
from datetime import datetime
current_date_and_time = datetime.now()
product_name = 0
product_quantity = 1
product_price = 2
sum = 0
sub_total = 0
price_of_item = 0
sales_tax_amount = 0
prdtcs = 'programming-with-functions\products\products.csv'
# userInpt = input('Enter item ID')
# user_quantity = int(input('Enter Quantity'))
req_file = 'programming-with-functions/products/request.csv'
print('Shop-Rite Supermarket')

with open(req_file, 'rt') as request:
    next_read = csv.reader(request)
    next(next_read)

    # initialized an empty array to store the items inside next_read after the loop
    req = []
    # looping through the items inside the next_read csv file
    for user_req in next_read:
        
        req.append(user_req)
    # print(req)


    # looping through the items inside the req array and assigning each items by index number to variables
    for keys in req:
        item_key = keys[0]
        item_count = keys[1]
        
        # summing up the total number of each goods 
        for numb in item_count:
            sum += int(numb)



        # Creating a function that 
        def read_dict(filename, key_column_index):
            sales_tax_amount = 0
            try:
                with open(filename, 'rt') as products:
                    reader = csv.reader(products)
                    # The first line of the CSV file contains
                    # headings and not fuel usage data, so this
                    # statement skips the first line of the file.
                    next(reader)
                    
                    # Storing the items inside the csv file as a dictionary of key and value pair
                    items = {}
                    sub_total = 0

                    # looping through the items inside the csv files and turning them into key:value pairs and assigning them to variables.
                    for lines in reader:
                        key = lines[product_name]
                        item_quantity = lines[1]

                        # looping through the prices of items and summing it up to get the subtotal
                        price_of_item = lines[2]
                        sub_total += float(price_of_item)

                        #  getting the sales tax amount
                        sales_tax_amount = sub_total/100 * 6
                        # Turning the product name into a key and the 2 values into a list to store them as a dictionary inside the items{}.
                        items[key] = [item_quantity, price_of_item]

                    # looping through the items inside the dictionary and assigning key value to each of them.
                    for item in items.items():
                        key = item[product_name]

                        # checking to see if the keys enterd by the user is thesame as any of the keys inside the dictionary and printing it out as an array
                        if key == key_column_index:
                            # looping through the values of the keys which is an array and assigning the values to variables
                            for goods in item:
                                description = goods[0]
                                price = goods[1]


                            print(f'{description}: {item_count} @ ${price} total ')
            except PermissionError as perm_err:
            # This code will be executed if the user enters the name
            # of a file and doesn't have permission to read that file.
                print()
                print(type(perm_err).__name__, perm_err, sep=": ")
                print(f"You don't have permission to read {filename}.")
                print("Run the program again and enter the name" \
                        " of a file that you are allowed to read.")

            except KeyError as key_err:
                # This code will be executed if the user enters
                # an invalid integer for the line number.
                print()
                print(type(key_err).__name__, key_err, sep=": ")
                print("You entered an invalid Key for the line number.")
                print("Run the program again and enter an integer for" \
                        " the line number.")

            except FileNotFoundError as not_found:
                print(type(not_found).__name__, not_found, sep=': ')
                print("Run the program again and enter an integer for" \
                        " the line number.")
            return sales_tax_amount, sub_total


        sales_tax, sub_total = read_dict(prdtcs, item_key)


    print(f'Date: {current_date_and_time:%A %I :%M %p}')
    print(f'The number of items in your cart is {sum}')
    print(f'The 6% sales tax is {sales_tax}')
    print(f'The total amount due is {sales_tax_amount + sub_total}')      
    print(f'Total payable amount is {sales_tax + sub_total}')
    print('Thank you for shopping in our store')

with open('programming-with-functions/accidentsfiles/receipt.txt', 'at') as receipt:
    print(f'Date: {current_date_and_time:%A %I :%M %p}\n'
        f'The number of items in your cart is {sum}\n'
        f'The 6% sales tax is {sales_tax}\n'
        f'The total amount due is {sales_tax_amount + sub_total}\n', file=receipt)
#         # clean = lines.strip()
#         # product.append(lines)
#         # print(price_of_item)
# # print(inpt)