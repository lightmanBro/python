# line_list = [' line 1\n', 'line 2 \n', ...]
# Generator expression -- returns iterator
# stripped_iter = (line.strip() for line in line_list)
# List comprehension -- returns list
# stripped_list = [line.strip() for line in line_list]

# stripped_list = [line.strip() for line in line_list
# if line != ""]


# Generator expressions are surrounded by parentheses (“()”) and list comprehensions are surrounded by square brackets
# (“[]”). Generator expressions have the form:
# ( expression for expr in sequence1
# if condition1
# for expr2 in sequence2
# if condition2
# for expr3 in sequence3 ...
# if condition3
# for exprN in sequenceN
# if conditionN )

def upper(s):
          return s.upper()

k = list(map(upper, ['sentence', 'fragment', 'booking', 'Assign']))
b = [upper(s) for s in ['sentence', 'fragment']]
print(k, b)