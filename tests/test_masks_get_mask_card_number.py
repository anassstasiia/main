import pytest

from src.masks import get_mask_card_number


def test_get_mask_card_number_standard():
    with pytest.raises(ValueError):
        get_mask_card_number(123456789012)


def test_get_card_number_short():
    with pytest.raises(ValueError):
        get_mask_card_number(12345678)


def test_get_mask_card_number_minimal():
    with pytest.raises(ValueError):
        get_mask_card_number(1)


def test_get_mask_card_number_invalid():
    with pytest.raises(ValueError):
        get_mask_card_number("")


def test_get_mask_card_number_with_valid(test_get_mask_card_number_valid):
    assert get_mask_card_number(test_get_mask_card_number_valid) == "7000 79** **** 6361"


@pytest.mark.parametrize(
    "card_number, expected", [(7000792289606361, "7000 79** **** 6361"), (1111222233334444, "1111 22** **** 4444")]
)
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected
