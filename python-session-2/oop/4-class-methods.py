class Animal:

  def __init__(self, name):
    self.name = name

  def whoami(self):
    return "My name is {}".format(self.name)

  def feed(self, food):
    return "My name is {0} and I want {1}".format(self.name, food)

  def display_kind(self):
    print("I am an Animal")

a1 = Animal("Lion")
print(a1.whoami())
print(a1.display_kind())
print(a1.feed("fruits"))