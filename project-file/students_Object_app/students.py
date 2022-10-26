class Student:
          #creating an initialize function to map out what attribute the student should have
          def __init__(self, name, major, gpa, is_on_probabtion):
                    self.name = name
                    self.major = major
                    self.gpa = gpa
                    self.is_on_probabtion = is_on_probabtion
          def on_honor_roll(self):
                    if self.gpa >= 3.5:
                              return True
                    else:
                              return False