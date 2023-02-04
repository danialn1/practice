from wallet import Wallet

def test_getBalance():
  obj=Wallet()
  obj.setBalance(20)
  assert obj.getBalance()==20
