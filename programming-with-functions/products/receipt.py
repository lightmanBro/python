import csv

product_name = 0
product_quantity = 1
product_price = 2
prdtcs = 'programming-with-functions\products\products.csv'
# userInpt = input('Enter item ID')
# user_quantity = int(input('Enter Quantity'))
req_file = 'programming-with-functions/products/request.csv'
print('Requested items')
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


        def read_dict(filename, key_column_index):
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
                    price_of_item = float(lines[2])
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
                        print(f'{description}: {item_count} @ ${price}')
            # print(items)
            return items
        read_dict(prdtcs, item_key)

#         # clean = lines.strip()
#         # product.append(lines)
#         # print(price_of_item)
# # print(inpt)