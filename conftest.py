import datetime
import pytest

from decimal import Decimal
from functions.level_1.four_bank_parser import BankCard, Expense, SmsMessage
from functions.level_2.two_students import Student


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
def bank_card_artem():
    return BankCard(last_digits="1111", owner="ARTEM")


@pytest.fixture
def bank_card_cat():
    return BankCard(last_digits="2222", owner="CAT")


@pytest.fixture
def cards(bank_card_artem, bank_card_cat):
    return [
        bank_card_artem,
        bank_card_cat,
    ]


@pytest.fixture
def expense(bank_card_cat):
    return Expense(
        amount=Decimal('10000'),
        card=bank_card_cat,
        spent_in="ZOO_BAR",
        spent_at=datetime.datetime(2023, 2, 18, 21, 15),
    )


@pytest.fixture
def student_ivanov():
    return Student("Ivan", "Ivanov", "@ivan")


@pytest.fixture
def student_petrov():
    return Student("Petr", "Petrov", None)


@pytest.fixture
def students(student_ivanov, student_petrov):
    return [student_ivanov, student_petrov]
