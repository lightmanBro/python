
# Appending new content to the file an existing file 'a'
from atexit import register


htmlFlie = open('register.txt', 'a')

# 'w' will override the content of the old file and delete it all adding just the new item to it.
htmlFlie = open('register.txt', 'w')

#adding to the list
htmlFlie.write('\nDavid - Computer Programmer')

htmlFlie.close()



# Creating a new file
# htmlFlie = open('py2.html', 'w')

# htmlFlie.write('\nDvaid - Computer Programmer')