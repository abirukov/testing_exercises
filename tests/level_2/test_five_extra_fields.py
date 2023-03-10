import pytest

from functions.level_2.five_extra_fields import fetch_extra_fields_configuration, fetch_app_config_field


@pytest.mark.parametrize(
    "config_filename, field_name, expected",
    [
        ("config.ini", "extra_fields", "\ntest: str"),
        ("config.ini", "no_fields", None),
        ("no_config.ini", "no_fields", None),
    ],
)
def test__fetch_app_config_field(config_filename: str, field_name: str, expected):
    assert fetch_app_config_field(f"tests/files/{config_filename}", field_name) == expected


@pytest.mark.parametrize(
    "config_filename, expected",
    [
        ("config.ini", {"test": str}),
        ("no_config.ini", {}),
    ],
)
def test__fetch_extra_fields_configuration(config_filename: str, expected):
    assert fetch_extra_fields_configuration(f"tests/files/{config_filename}") == expected
