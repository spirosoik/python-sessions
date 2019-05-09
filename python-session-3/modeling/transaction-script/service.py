from models import (
  Account,
  NEVER_OVERDRAFT_POLICY,
  ALLOWED_OVERDRAFT_POLICY
)
from exceptions import DebitException


class MoneyTransfer:

  def transfer(self, from_account, to_account, amount):
    pass


class MoneyTransferService(MoneyTransfer):
  __limit = 1000

  def transfer(self, from_account, to_account, amount):

    new_balance = from_account.balance - amount

    if from_account.overdraft_policy == NEVER_OVERDRAFT_POLICY:
      if new_balance < 0:
        raise DebitException("Insufficient Funds")

    elif from_account.overdraft_policy == ALLOWED_OVERDRAFT_POLICY:
      if new_balance < -self.__limit:
        limit = self.__limit
        raise DebitException(
          f"Overdraft limit (of {limit}) exceeded: {new_balance}"
        )

    from_account.balance = new_balance
    to_account.balance = to_account.balance + amount

    print(f'From Account Balance: {from_account.balance}')
    print(f'To Account Balance: {to_account.balance}')

    return "Money transferred successfully"
