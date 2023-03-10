import pytest

from functions.level_2.one_brackets import delete_remove_brackets_quotes


@pytest.mark.parametrize(
    'name, expected',
    [
        ('{"test_name"}', 'test_name'),
        ('test_name', 'test_name'),
    ],
)
def test__delete_remove_brackets_quotes(name: str, expected: str) -> None:
    assert delete_remove_brackets_quotes(name) == expected
