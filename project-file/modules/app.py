
'''
MODULES:
it is used to better organize our codes
and also to use a specific important part we need out of a whole big other projects.
'''

'''
importing the whole module'''
import converters 
print(converters.kg_to_lbs(70))




'''
importing specific functions of a class from the whole modules.
this allows us to directly call the function without the ( . ) method notation
'''
from converters import kg_to_lbs
kg_to_lbs(120)


