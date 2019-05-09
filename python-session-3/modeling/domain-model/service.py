from exceptions import DebitException


class OverdraftPolicy:

  def __init__(self, limit=0):
    self.limit = limit

  def pre_debit(self, account, amount):
    pass

  def post_debit(self, account, amount):
    pass


class NoOverdraftAllowed(OverdraftPolicy):

  def pre_debit(self, account, amount):
    new_balance = account.balance - amount
    if new_balance < 0:
      raise DebitException("Insufficient Funds")


class LimitedOverdraft(OverdraftPolicy):

  def pre_debit(self, account, amount):
    new_balance = account.balance - amount
    if new_balance < -self.limit:
      limit = self.limit
      raise DebitException(
        f"Overdraft limit (of {limit}) exceeded: {new_balance}"
      )


class MoneyTransfer:

  def transfer(self, from_account, to_account, amount):
    pass


class MoneyTransferService(MoneyTransfer):

  def transfer(self, from_account, to_account, amount):
    from_account.debit(amount)
    to_account.credit(amount)

    print(f'From Account Balance: {from_account.balance}')
    print(f'To Account Balance: {to_account.balance}')

    return "Money transferred successfully"
