import pytest

from src.widget import get_date


def test_get_date_with_fixture(test_get_date_fixture):
    assert get_date(test_get_date_fixture) == "11.03.2024"


def test_get_date_len():
    with pytest.raises(ValueError):
        get_date("22-05-10T02:26:18.671407")


def test_get_date_letters():
    with pytest.raises(ValueError):
        get_date("AAAA-05-10T02:26:18.671407")


def test_get_date_empty():
    with pytest.raises(ValueError):
        get_date("")


@pytest.mark.parametrize(
    "data, expected", [("2024-03-11T02:26:18.671407", "11.03.2024"), ("2022-05-10T02:26:18.671407", "10.05.2022")]
)
def test_get_date(data, expected):
    assert get_date(data) == expected
