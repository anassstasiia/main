import pytest

from src.widget import mask_account_card


def test_mask_account_card_without_space():
    with pytest.raises(ValueError):
        assert mask_account_card("Visa Platinum1412151215121212")


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("Visa Platinum 1256487896542135", "Visa Platinum 1256 48** **** 2135"),
        ("MasterCard 1212514789541254", "MasterCard 1212 51** **** 1254"),
        ("Visa Gold 4547484564525456", "Visa Gold 4547 48** **** 5456"),
        ("Счет 11111222225555588888", "Счет **8888"),
    ],
)
def test_mask_account_card(account_number, expected):
    assert mask_account_card(account_number) == expected


def test_mask_account_card_with_valid(test_mask_account_card_valid):
    assert mask_account_card(test_mask_account_card_valid) == "Visa Platinum 1256 48** **** 2135"
