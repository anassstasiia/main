import pytest

from src.masks import get_mask_account


def test_get_mask_account_minimal():
    with pytest.raises(ValueError):
        get_mask_account(25)


def test_get_mask_account_min_four():
    with pytest.raises(ValueError):
        get_mask_account(354)


def test_get_mask_account_short_standard():
    with pytest.raises(ValueError):
        get_mask_account(12548456)


@pytest.mark.parametrize(
    "mask_account, expected",
    [(73654108430135874305, "**4305")],
)
def test_get_mask_account(mask_account, expected):
    assert get_mask_account(mask_account) == expected


def test_get_mask_account_fixture(test_get_mask_account_standard):
    assert get_mask_account(test_get_mask_account_standard) == "**4305"
