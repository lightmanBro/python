# 'r' = read, 'w' = write, 'a' = append, 'r+' = read and write.

#opening a file
htmlFlie = open('register.txt', 'r' )


# checking if the file is readable or not.
print(htmlFlie.readable())

#this will print out the contents of the file
print(htmlFlie.read())

# to read individual lines of the file
print(htmlFlie.readline())

#this will take all the lines in the file and print it as an array and the lines can be acessed like an array too.
print(htmlFlie.readlines()[1])


#using a for loop
for elements in htmlFlie.readlines():
          print(elements)


#closing the file
htmlFlie.close()



