
from bdb import checkfuncname

'''
using inheritance in modules that has almost thesame functions
'''
from chef import Chef
class ChineseChef(Chef): #we will be able to use all the functions inside the Chef module here and also the unique function of this module.

          # overriding the special dishes function in the chef module and defining a special one for ChineseChef.
          def make_special_dishes(self):
                  print('This Chef makes Orange Chicken')
          def make_fried_rice(self):
                    print('The chef makes fried rice')




# #First Method:
# class ChineseChef:
#           def make_chicken(self):
#                     print('The chef makes a chicken')
#           def make_salad(self):
#                     print('The chef makes a salad')

#           def make_special_dishes(self):
#                     print('The chef makes a orange chicken')
          
#           def make_fried_rice(self):
#                     print('The chef makes fried rice')
