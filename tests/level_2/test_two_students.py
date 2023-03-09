import pytest

from functions.level_2.two_students import get_student_by_tg_nickname, Student


@pytest.mark.parametrize(
    "telegram_username, students_list, expected",
    [
        ("ivan", pytest.lazy_fixture("students"), pytest.lazy_fixture("student_ivanov")),
        ("petr", pytest.lazy_fixture("students"), None),
    ],
)
def test__get_student_by_tg_nickname(telegram_username: str, students_list: list[Student], expected: Student):
    print(students_list)
    assert get_student_by_tg_nickname(telegram_username, students_list) == expected
