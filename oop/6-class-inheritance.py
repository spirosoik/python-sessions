class Animal:

  def __init__(self):
    print("Animal created")

  def who_am_i(self):
    print("Animal")

  def eat(self):
    print("Eating")

  def need_water(self):
    return True


class Dog(Animal):

  def __init__(self):
    print("Dog created")

  def who_am_i(self):
    print("Dog")

  def bark(self):
    print("Woof!")

  def eat(self):
    print("Meat")

class Cat(Animal):

  def __init__(self):
    print("Cat created")

  def who_am_i(self):
    print("Cat")

class Lion(Animal):

  def __init__(self):
    print("Lion created")

  def who_am_i(self):
    print("Lion")


d = Dog()
c = Cat()
l = Lion()
d.who_am_i()
d.need_water()
c.who_am_i()
c.need_water()
l.who_am_i()
l.need_water()
# d.eat()
