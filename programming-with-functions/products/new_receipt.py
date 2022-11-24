import csv
from datetime import datetime
current_date_and_time = datetime.now()
product_name = 0
product_quantity = 1
product_price = 2
sub_total = 0
price_of_item = 0
# sub_total = 0
sales_tax_amount = 0
item_key = ''
item_count = 0
description = ''
price = 0

request_file = []

prdtcs = 'programming-with-functions\products\products.csv'
# userInpt = input('Enter item ID')
# user_quantity = int(input('Enter Quantity'))
req_file = 'programming-with-functions/products/request.csv'
print('Shop-Rite Supermarket')




sum = 0
try:
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
            # print(item_key, item_count)
except PermissionError as perm_err:
        # This code will be executed if the user enters the name
        # of a file and doesn't have permission to read that file.
        print()
        print(type(perm_err).__name__, perm_err, sep=": ")
        print(f"You don't have permission to read {req_file}.")
        print("Run the program again and enter the name" \
                " of a file that you are allowed to read.")

except ValueError as val_err:
    # This code will be executed if the user enters
    # an invalid integer for the line number.
    print()
    print(type(val_err).__name__, val_err, sep=": ")
    print("You entered an invalid integer for the line number.")
    print("Run the program again and enter an integer for" \
            " the line number.")
except FileNotFoundError as not_found:
    print(type(not_found).__name__, not_found, sep=': ')


def read_prod(filename,key_column_index):
    sub_total = 0
    sales_tax_amount = 0
    key = ''
    try:
        with open(filename, 'rt') as products:
            reader = csv.reader(products)
            # The first line of the CSV file contains
            # headings and not fuel usage data, so this
            # statement skips the first line of the file.
            next(reader)
            
            # Storing the items inside the csv file as a dictionary of key and value pair
            items = {}

            # looping through the items inside the csv files and turning them into key:value pairs and assigning them to variables.
            for lines in reader:
                key = lines[product_name]
                item_quantity = lines[1]

                # looping through the prices of items and summing it up to get the subtotal
                price_of_item = lines[2]
                sub_total += float(price_of_item)

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



            print(f'The Sub total Price of the goods is ${sub_total}')
            # to get the sales tax amount we will divide subtotal and multiply it by 6% 
            sales_tax_amount = sub_total/100 * 6
            print(f'The number of items in your cart is {sum}') 
            print(f'Date: {current_date_and_time:%A %I :%M %p}')   
            print(f'The 6% Sales Tax is ${sales_tax_amount}')
            print(f'The total amount due is {sales_tax_amount + sub_total}')

        
    except PermissionError as perm_err:
            # This code will be executed if the user enters the name
            # of a file and doesn't have permission to read that file.
            print()
            print(type(perm_err).__name__, perm_err, sep=": ")
            print(f"You don't have permission to read {filename}.")
            print("Run the program again and enter the name" \
                    " of a file that you are allowed to read.")

    except ValueError as val_err:
        # This code will be executed if the user enters
        # an invalid integer for the line number.
        print()
        print(type(val_err).__name__, val_err, sep=": ")
        print("You entered an invalid integer for the line number.")
        print("Run the program again and enter an integer for" \
                " the line number.")
    except FileNotFoundError as not_found:
        print(type(not_found).__name__, not_found, sep=': ')

    return items, sub_total


items, subtotal = read_prod(prdtcs,req_file)
for item in items.items():
    item_keys = item[0]
    item_description = item[1]
    if item_keys in item:
        print(item)
print( subtotal)