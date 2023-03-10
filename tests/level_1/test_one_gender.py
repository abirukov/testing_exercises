import pytest

from functions.level_1.one_gender import genderalize


@pytest.mark.parametrize(
    "verb_male, verb_female, gender, expected",
    [
        ("Делал", "Делала", "male", "Делал"),
        ("Делал", "Делала", "female", "Делала"),
    ],
)
def test__genderalize(verb_male: str, verb_female: str, gender: str, expected: str):
    assert genderalize(verb_male, verb_female, gender) == expected
