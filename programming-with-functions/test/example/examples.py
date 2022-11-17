def addr(str):
    str = str.strip()
    lastCommaIndx = str.rindex(',')
    midcoma = str.rindex(',', 0, lastCommaIndx)
    city = str[midcoma + 1 : lastCommaIndx]
    city = city.strip()
    print(midcoma)
    print(lastCommaIndx)
    print(city)
    return city

res = addr("123 W Main, Rexburg, ID 83440")
print(res)
# print(comaInd)
# print(lastCommaIndx)
# print(city)

# full_address = full_address.strip()
# last_comma_index = full_address.rindex(",")
# mid_comma_index = full_address.rindex(",", 0, last_comma_index)
# city = full_address[mid_comma_index + 1 : last_comma_index]
# city = city.strip()
# return city