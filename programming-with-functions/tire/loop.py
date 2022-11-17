
key = ''
dictionary = {}
value = []

while key != 'finish':
    key = input('Enter the key')
    val = int(input('Enter the value'))
    if key in dictionary:
        print(key)
    dictionary[key] = val
    

print(dictionary)