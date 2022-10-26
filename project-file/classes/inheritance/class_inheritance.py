'''
Inheritance is a specific value or function that is applicable to series of objects irrespective of their types e. one thing they have in common.
'''
class Mammal:
          def walk(self):
                    print('Walk')

# the Dog class getting an inheritance value as a parameter so that it can have acess to it
class Dog(Mammal):
          def bark(self):
                    print('Bark!!')


# the Cat class getting an inheritance value as a parameter so that it can have acess to it
class Cat(Mammal):
          def mew(self):
                    print('Meow...')


dog1 = Dog()
dog1.bark()
cat1 = Cat()
cat1.mew()
