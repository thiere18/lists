from _pytest.fixtures import fixture
import pytest
from app.calculation import BankAccount, add ,BankAccount ,InsufficientFunds
@pytest.mark.parametrize("num1,num2,result",
[(3,2,5),(6,6,12),(1,2,3),(1,3,4)]
)
def test_add(num1,num2,result):
    assert add(num1,num2)==result

@pytest.fixture
def zero_bank():
    return BankAccount()

@pytest.fixture
def inital_bank():
    return BankAccount(50)

def test_starting(zero_bank):
    assert zero_bank.balance==0
    
def test_deposit(inital_bank):
    inital_bank=BankAccount(50)
    inital_bank.deposit(50)
    assert inital_bank.balance==100

def test_withdraw(inital_bank):
    inital_bank.withdraw(40)
    assert inital_bank.balance==10

def test_interest(inital_bank):
    inital_bank.deposit(50)
    inital_bank.collect_interest()
    assert round(inital_bank.balance,5)==110

@pytest.mark.parametrize("deposit,withdraw ,expected",[(200,100,100),(200,50,150)])
def test_transaction(zero_bank,deposit,withdraw,expected):
    zero_bank.deposit(deposit)
    zero_bank.withdraw(withdraw)

    assert zero_bank.balance==expected

def test_insufficient_balance(zero_bank):
    with pytest.raises(InsufficientFunds):
        zero_bank.withdraw(101)