from models import Account
from service import (
  LimitedOverdraft,
  MoneyTransferService,
  NoOverdraftAllowed
)

service = MoneyTransferService()
from_account = Account(1, 5000, LimitedOverdraft(1000))
to_account = Account(2, 10000, NoOverdraftAllowed())

status = service.transfer(from_account, to_account, 6000)
print(status)
