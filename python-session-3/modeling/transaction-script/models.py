NEVER_OVERDRAFT_POLICY = 'NEVER'
ALLOWED_OVERDRAFT_POLICY = 'ALLOWED'


class Account:
  def __init__(self, id, balance, overdraft_policy):
    self.id = id
    self.balance = balance
    self.overdraft_policy = overdraft_policy
