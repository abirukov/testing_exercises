import datetime
import pytest

from functions.level_1.two_date_parser import compose_datetime_from


def datetime_midday_from_today(add_days=0):
    today = datetime.date.today()
    return datetime.datetime(today.year, today.month, today.day + add_days, 12, 0)


datetime_today_midday = datetime_midday_from_today()
datetime_tomorrow_midday = datetime_midday_from_today(1)


@pytest.mark.parametrize(
    "date_str, time_str, expected",
    [
        ("today", "12:00", datetime_today_midday),
        ("tomorrow", "12:00", datetime_tomorrow_midday),
    ],
)
def test__compose_datetime_from(date_str: str, time_str: str, expected: datetime.datetime):
    assert compose_datetime_from(date_str, time_str) == expected
