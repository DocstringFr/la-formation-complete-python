from bank import Account
import pytest


@pytest.fixture
def account():
    return Account(initial_balance=1000)


def test_deposit(account):
    account.deposit(amount=1000)
    assert account.balance == 2000


def test_withdraw(account):
    account.withdraw(amount=500)
    assert account.balance == 500


def test_withdraw_not_enough_money():
    account = Account(initial_balance=200)
    with pytest.raises(ValueError):
        account.withdraw(amount=500)


def test__create_identifier_length_of_identifier(account):
    assert len(account.identifier) == 25


def test__create_identifier_is_alnum(account):
    assert account.identifier.isalnum() is True
