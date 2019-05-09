class Medication:
  def __init__(self, pill):
    self.pill = pill


class Animal:

  def __init__(self, name='', medication=None):
    self.name = name
    self.medication = medication

  def talk(self):
    pass

  def show_medication(self):
    if self.medication is None:
      print("No medication")
      return

    print(f"Medication Pill: {self.medication.pill}")


class Cat(Animal):

  def talk(self):
    print("Meow!")


a = Animal()
a.talk()

c = Cat("Missy", Medication("aspirine"))
c.talk()
c.show_medication()
