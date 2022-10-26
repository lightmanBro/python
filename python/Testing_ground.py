'''
WORD SLICING
'''
word = 'python'
word[1:5] # print word from index of 1 to 5 it will Print [ython]
word[-1] # means the last word from the back should be printed
word[:2] + word[2:]
'Python'

# +---+---+---+---+---+---+ 
# | P | y | t | h | o | n | 
# +---+---+---+---+---+---+ 
#   0  1   2   3   4   5 6 
#   -6 -5 -4 -3 -2 -1
# word[0] = 'j' # will throw an error

'j' + word[1:]
'Jython'
word[:2] + 'py'
'Pypy'


'''
LEN()
'''
# len() # returns the lenght of a string and lists
s = 'supercalifragilisticexpialidocious'
len(s)
34

'''
LISTS
like strings and all other built-in sequence types,  strings can be indexed and sliced and also can be concatenated with other lists,  len() can also be used on lists, lists allows nesting also:
'''
# indexing
squares = [1, 4, 9, 16, 25]
squares[0]
1
print(squares[-1])
25

# slicing
print(squares[-3:])
[9, 16, 25]
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# replacing values letters[2 to 5] = letters[2:5]
letters[2:5] = ['C', 'D', 'E']
['a', 'b', 'C', 'D', 'E', 'f', 'g']
# removing values
letters[2:5] = []
['a', 'b', 'f', 'g']
# clearing the values
letters[:] = []
[]



# concatenation
# squares + [36, 49, 12, 67]
# squares + range(20, 60, 5) # this will throw an error unless we append it to a new variable so that it can be turned into a list then we can now concatenate it with another list
numb = []
for rg in range(20, 60, 5):
          numb.append(rg)
new = numb + squares # add the contents of the two lists togeher and store it in variable (new).
print(sorted(new)) # sort the list and print the sorted new list.
value1 = [1, 4, 9, 16, 20, 25, 25, 30, 35, 40, 45, 50, 55]


a, b = 0, 1
while a < 1000:
          print(a, end=',') # the answers at each iteration will be ended by (,)
          a, b = b, a + b
value2 = 0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,
print()

# iterating over indices and sequence using len() and range()
for i in range(len(value2)):
          print(i +1, value2[i]) #sum(range(i))

# range() cannot work for string, it can only work for int, but enumerate() and len() can work for strings
a = ['Mary', 'had', 'a', 'little', 'lamb']
for b in enumerate(a):
          print(b, len(b))
# for b in len(a):
#           print(b)

sum(range(4)) # 0 + 1 + 2 + 3
6

'''
break AND continue AND else CLAUSE ON loops
'''
for n in range(2, 10):
          for x in range(2, n):
                    if n % x == 0:
                              print(n, 'equals', x, '*', n//x)
                              break
          else:
          # this else statement is meant for the for loop
          # if loop fell through without finding a factor
                    print(n, 'is a prime number')


'''
A match statement takes an expression and compares its value to successive patterns given as one or more case
blocks. This is superficially similar to a switch statement in C, Java or JavaScript (and many other languages), but it
can also extract components (sequence elements or object attributes) from the value into variables.
'''
status = int(input('Enter: '))
def http_error_socket(status):
          match status:
                    case 1:
                              return 'one'
                    case 2:
                              return 'two'
                    case 3:
                              return 'three'
                    case 4 | 5| 6:
                              return 'out of range'
                    case _:
                              return 'this number is not recognized'
v = http_error_socket(status)
print(v)

