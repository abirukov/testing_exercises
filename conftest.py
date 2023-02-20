import datetime
import pytest

from _decimal import Decimal
from functions.four_bank_parser import BankCard, Expense, SmsMessage


@pytest.fixture
def valid_ineco_expense_sms_text():
    return "10000 RUR, 5555444433332222 18.02.23 21:15 ZOO_BAR authcode 3456"


@pytest.fixture
def sms(valid_ineco_expense_sms_text):
    return SmsMessage(
        text=valid_ineco_expense_sms_text,
        author="ARTEM",
        sent_at=datetime.datetime.now(),
    )


@pytest.fixture
def cards():
    return [
        BankCard(last_digits="1111", owner="ARTEM"),
        BankCard(last_digits="2222", owner="CAT"),
    ]


@pytest.fixture
def expense():
    return Expense(
        amount=Decimal('10000'),
        card=BankCard(last_digits="2222", owner="CAT"),
        spent_in="ZOO_BAR",
        spent_at=datetime.datetime(2023, 2, 18, 21, 15),
    )
