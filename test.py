from wallet import Wallet

def test_getBalance():
  obj=Wallet()
  obj.setAmount(20)
  assert obj.getAmount()==20
