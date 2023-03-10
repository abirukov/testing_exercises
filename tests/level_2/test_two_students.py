import pytest

from functions.level_2.two_students import get_student_by_tg_nickname, Student


@pytest.mark.parametrize(
    "telegram_username, expected",
    [
        ("ivan", pytest.lazy_fixture("student_ivanov")),
        ("petr", None),
    ],
)
def test__get_student_by_tg_nickname(telegram_username: str, students: list[Student], expected: Student):
    assert get_student_by_tg_nickname(telegram_username, students) == expected
