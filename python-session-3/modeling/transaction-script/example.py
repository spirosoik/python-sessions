from models import (
  Account,
  NEVER_OVERDRAFT_POLICY,
  ALLOWED_OVERDRAFT_POLICY
)
from service import MoneyTransferService

service = MoneyTransferService()
from_account = Account(1, 5000, ALLOWED_OVERDRAFT_POLICY)
to_account = Account(2, 10000, NEVER_OVERDRAFT_POLICY)

status = service.transfer(from_account, to_account, 6001)
print(status)