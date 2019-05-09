class Animal:

  def __init__(self, name=None, gender=None):
    self.name = name
    self.gender = gender


a1 = Animal(gender="male")
print(a1.name)
