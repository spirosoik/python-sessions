class Animal:

  def __init__(self, name):
    self.__name = name

  def whoami(self):
    return "My name is {}".format(self.__name)

  def feed(self, food):
    return "My name is {0} and I want {1}".format(self.__name, food)

  def display_kind(self):
    print(self.__name)

  def __gender(self):
    return "male"


a1 = Animal("Lion")
print(a1.__name)
