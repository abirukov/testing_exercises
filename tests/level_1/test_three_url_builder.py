import pytest

from functions.level_1.three_url_builder import build_url
from typing import Mapping


@pytest.mark.parametrize(
    "expected, host_name, relative_url, get_params",
    [
        (
            "https://market.yandex.ru/catalog",
            "https://market.yandex.ru",
            "catalog",
            None,
        ),
        (
            "https://market.yandex.ru/catalog",
            "https://market.yandex.ru",
            "catalog",
            {},
        ),
        (
            "https://market.yandex.ru/catalog?product_id=1&color=red",
            "https://market.yandex.ru",
            "catalog",
            {
                "product_id": "1",
                "color": "red",
            },
        ),
    ],
)
def test__build_url(
    expected: str,
    host_name: str,
    relative_url: str,
    get_params: Mapping[str, str],
):
    assert build_url(host_name, relative_url, get_params) == expected
