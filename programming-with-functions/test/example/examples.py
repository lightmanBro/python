
import re
def addr(str):
    str = str.strip()
    lastCommaIndx = str.rindex(',')
    midcoma = str.rindex(',', 0, lastCommaIndx)
    city = str[midcoma + 1 : lastCommaIndx]
    city = city.strip()
    print(midcoma)
    print(lastCommaIndx)
    print(city)
    print(city)

res = addr("123 W Main, Rexburg, ID 83440")
print(res)


# def addr(str):
#     # str = str.strip()
#     # print(str.strip())
#     lastCommaIndx = str.rindex(' ')
#     print(lastCommaIndx)
#     midcoma = str.rindex(' ', 0, lastCommaIndx)
#     print(midcoma)
#     city = str[midcoma + 1 : lastCommaIndx]

#     city = city.strip()
#     print(midcoma)
#     print(lastCommaIndx)
#     # print(city) 
#     return city

# res = addr(" 123 W Main, Rexburg, ID 83440 ")
# print(res)
# print(comaInd)
# print(lastCommaIndx)
# print(city)

# full_address = full_address.strip()
# last_comma_index = full_address.rindex(",")
# mid_comma_index = full_address.rindex(",", 0, last_comma_index)
# city = full_address[mid_comma_index + 1 : last_comma_index]
# city = city.strip()
# return city
text = '123 W Main, Rexburg, ID 83440'
# lastCommaIndx = str.rindex(' ')
# Acessing the contents of the list by index number from position 3 till the end of the list.
t = text[3: -1]
print(t)

# Example 1
# Counting the number of an occurence of a space or character in a string
def checkspace(string):
    count = 0

    for i in string:
        if i == ' ':
            count += 1
    print(count)
            # print(i+1)

# Example 2
def check_space(string):
    return string.count(' ')

# Example 3
c = 0
for i in text:
    if(i.isspace()):
        c+=1
print('number of spaces : ' +str(c) )
print(check_space(text + '2'))

checkspace(text)