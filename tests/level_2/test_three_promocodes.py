import re

from functions.level_2.three_promocodes import generate_promocode


def test__generate_promocode():
    promocode = generate_promocode()
    match_result = re.match(r"^[A-Z]{" + str(len(promocode)) + "}", promocode)
    assert match_result.group(0) is not None
