import pytest
from Checkout import *


@pytest.fixture()
def checkout():
    checkout1 = Checkout()
    checkout1.addItemPrice('a', 5)
    checkout1.addItemPrice('b', 2)
    return checkout1


def test_canInitiateClass(checkout):
    checkout


def test_canAddItemPrice(checkout):
    checkout.addItemPrice("a", 5)


def test_canAddItem(checkout):
    checkout.addItem("a")


def test_canCalculateTotal(checkout):
    checkout.addItem('a')
    checkout.addItem('a')
    checkout.addItem('b')
    assert checkout.calculateTotal() == 12


def test_canApplyDisRule(checkout):
    checkout.addDiscount('a', 3, 2)


def test_canApplyDiscount(checkout):
    checkout.addDiscount('a', 3, 2)
    checkout.addItem('a')
    checkout.addItem('a')
    checkout.addItem('a')
    checkout.addItem('a')
    checkout.addItem('b')
    total = checkout.calculateTotal()
    assert total == 13


def test_exceptionWithBadItem(checkout):
    with pytest.raises(Exception):
        checkout.addItem('c')
