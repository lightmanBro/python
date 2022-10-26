from msilib.schema import Directory
from pathlib import Path

'''
Importing files have 2 options:
Absolute path: from root directory c:\Program\
Relative path: is a path that is in thesame folder with the code we are writing
'''

# path = Path('emails')
# print(path.exist()) if path exists
# print(path.mkdir()) making a directory
# print(path.rmdir()) removing a directory

'''
finding files in a directory, iterating over all the directories and processing them.
'''
path = Path()
# #for all files in all the directories
# print(path.glob('*')) 
# # for all the files in this specific current Directory
# print(path.glob('*.*')) 

# # for all the files with a specific extension etc
# print(path.glob('*.extension')) 

for file in path.glob('*'):
          print(file)  