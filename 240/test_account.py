from account import Account
import pytest
# write your test functions below, they need to start with test_

bob = Account('bob')
julien = Account('julien', 15)

def test_account_balance():
    assert bob.amount == 0
    bob.add_transaction(10)
    assert bob.balance == 10
    with pytest.raises(ValueError) as e:
        bob.add_transaction('a')
    assert str(e.value) == "please use int for amount"
    with pytest.raises(ValueError) as e:
        bob.add_transaction('')
    assert str(e.value) == "please use int for amount"
    with pytest.raises(ValueError) as e:
        bob.add_transaction('1')
    assert str(e.value) == "please use int for amount"
    with pytest.raises(ValueError) as e:
        bob.add_transaction({})
    assert str(e.value) == "please use int for amount"
    with pytest.raises(ValueError) as e:
        julien.add_transaction([])
    assert str(e.value) == "please use int for amount"
    bob.add_transaction(-5)
    assert bob.balance == 5


def test_account_comparison():
    assert julien > bob
    assert julien >= bob
    assert bob < julien
    assert bob <= julien
    julien.add_transaction(-5)
    bob.add_transaction(5)
    assert bob == julien


def test_account_len():
    julien.add_transaction(15)
    julien.add_transaction(13)
    julien.add_transaction(-7)
    assert len(julien) == 4


def test_account_indexing_iter():
    assert julien[0] == -5
    assert julien[-1] == -7
    assert list(julien) == [-5, 15, 13, -7]
    


def test_account_repr():
    assert repr(julien) == "Account('julien', 15)"
    assert repr(bob) == "Account('bob', 0)"


def test_account_str():
    assert str(julien) == 'Account of julien with starting amount: 15'
    assert str(bob) == 'Account of bob with starting amount: 0'

def test_account_add():
    assert str(bob + julien) == 'Account of bob&julien with starting amount: 15'
    

