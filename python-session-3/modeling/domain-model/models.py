class Account:
  def __init__(self, id, balance, overdraft_policy):
    self.id = id
    self.balance = balance
    self.overdraft_policy = overdraft_policy

  def debit(self, amount):
    self.overdraft_policy.pre_debit(self, amount)
    self.balance = self.balance - amount
    self.overdraft_policy.post_debit(self, amount)

  def credit(self, amount):
    self.balance = self.balance + amount
