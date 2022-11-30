import re

words = ['bank', 'troops', 'maker', 'outcast', 'bake', 'bankole']

# userInpt = input('Enter key: ')
# for word in words:
#     if userInpt in word:
#         print(word)

userInpt = input('Enter key: ')
for word in words:
    if userInpt in word and len(userInpt) >= 3:
       print(word)
    else:
        print('Key not found')
# SEARCH AND REPLACE
p = re.compile('(blue|white|red)')
p.sub('colour', 'blue socks and red shoes')
'colour socks and colour shoes'
res = p.sub('colour', 'blue socks and red shoes', count=1)
'colour socks and red shoes'
print(res)