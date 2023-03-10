from functions.level_1.four_bank_parser import BankCard, SmsMessage, Expense, parse_ineco_expense


def test__parse_ineco_expense(sms: SmsMessage, cards: list[BankCard], expense: Expense):
    assert parse_ineco_expense(sms, cards) == expense
