import pytest

from functions.level_2.four_lines_counter import count_lines_in


@pytest.mark.parametrize(
    "filepath, expected",
    [
        ("tests/files/no_file.txt", None),
        ("tests/files/empty_file.txt", 0),
        ("tests/files/five_lines_file.txt", 5),
    ],
)
def test__count_lines_in(filepath: str, expected):
    assert count_lines_in(filepath) == expected
